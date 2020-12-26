This is ${foo}
Copyright Linus Torvalds ${years(2007)}

% for a in range(10):
    ${a}
% endfor

<%
    import platform
    hostname=platform.node()
%>

You are running on ${hostname}

This checks if a variable is in a mako dict or not...
http://stackoverflow.com/questions/18624290/how-to-check-if-a-key-exists-in-mako-dict
% if 'a' in d:
    ${d['a']}
    'a' is in d
% else:
    'a' is not in d
% endif

next line will not be shown since lines starting with ## are a comment in mako templates

## this is a comment

next line will be shown...

<%text>## this is a comment</%text>
