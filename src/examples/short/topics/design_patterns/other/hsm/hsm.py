"""
Implementation of the HSM (hierarchical state machine) or
NFSM (nested finite state machine) C++ example from
http://www.eventhelix.com/RealtimeMantra/HierarchicalStateMachine.htm#.VwqLVEL950w
in Python

- single source "message type" for state transition changes
- message type considered, messages (comment) not considered to avoid complexity
"""


class UnsupportedMessageType(BaseException):
    pass


class UnsupportedState(BaseException):
    pass


class UnsupportedTransition(BaseException):
    pass


class HierachicalStateMachine:
    def __init__(self):
        self.active_state = Active(self)  # Unit.Inservice.Active()
        self.standby_state = Standby(self)  # Unit.Inservice.Standby()
        self.suspect_state = Suspect(self)  # Unit.OutOfService.Suspect()
        self.failed_state = Failed(self)  # Unit.OutOfService.Failed()
        self.current_state = self.standby_state
        self.states = {
            "active": self.active_state,
            "standby": self.standby_state,
            "suspect": self.suspect_state,
            "failed": self.failed_state,
        }
        self.message_types = {
            "fault trigger": self.current_state.on_fault_trigger,
            "switchover": self.current_state.on_switchover,
            "diagnostics passed": self.current_state.on_diagnostics_passed,
            "diagnostics failed": self.current_state.on_diagnostics_failed,
            "operator inservice": self.current_state.on_operator_inservice,
        }

    def next_state(self, state):
        try:
            self.current_state = self.states[state]
        except KeyError as e:
            raise UnsupportedState from e

    def send_diagnostics_request(self):
        return "send diagnostic request"

    def raise_alarm(self):
        return "raise alarm"

    def clear_alarm(self):
        return "clear alarm"

    def perform_switchover(self):
        return "perform switchover"

    def send_switchover_response(self):
        return "send switchover response"

    def send_operator_inservice_response(self):
        return "send operator inservice response"

    def send_diagnostics_failure_report(self):
        return "send diagnostics failure report"

    def send_diagnostics_pass_report(self):
        return "send diagnostics pass report"

    def abort_diagnostics(self):
        return "abort diagnostics"

    def check_mate_status(self):
        return "check mate status"

    def on_message(self, message_type):  # message ignored
        if message_type in self.message_types:
            self.message_types[message_type]()
        else:
            raise UnsupportedMessageType


class Unit(HierachicalStateMachine):
    def __init__(self, hierachicalStateMachine):
        super().__init__()
        self.hsm = hierachicalStateMachine

    def on_switchover(self):
        raise UnsupportedTransition

    def on_fault_trigger(self):
        raise UnsupportedTransition

    def on_diagnostics_failed(self):
        raise UnsupportedTransition

    def on_diagnostics_passed(self):
        raise UnsupportedTransition

    def on_operator_inservice(self):
        raise UnsupportedTransition


class Inservice(Unit):
    def on_fault_trigger(self):
        self.hsm.next_state("suspect")
        self.hsm.send_diagnostics_request()
        self.hsm.raise_alarm()

    def on_switchover(self):
        self.hsm.perform_switchover()
        self.hsm.check_mate_status()
        self.hsm.send_switchover_response()


class Active(Inservice):
    def on_fault_trigger(self):
        super().perform_switchover()
        super().on_fault_trigger()

    def on_switchover(self):
        self.hsm.on_switchover()  # message ignored
        self.hsm.next_state("standby")


class Standby(Inservice):
    def on_switchover(self):
        super().on_switchover()  # message ignored
        self.hsm.next_state("active")


class OutOfService(Unit):
    def on_operator_inservice(self):
        self.hsm.on_switchover()  # message ignored
        self.hsm.send_operator_inservice_response()
        self.hsm.next_state("suspect")


class Suspect(OutOfService):
    def on_diagnostics_failed(self):
        super().send_diagnostics_failure_report()
        super().next_state("failed")

    def on_diagnostics_passed(self):
        super().send_diagnostics_pass_report()
        super().clear_alarm()  # loss of redundancy alarm
        super().next_state("standby")

    def on_operator_inservice(self):
        super().abort_diagnostics()
        super().on_operator_inservice()  # message ignored


class Failed(OutOfService):
    """No need to override any method."""
