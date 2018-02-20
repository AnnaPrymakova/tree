def buildSub(d, level, first, skipPipe):
    symbol = ' ' if skipPipe else '|';
    for word in d.split():
        if first:
            prefix = ''
            if (level > 0):
                prefix = ('    ' * (level-1))[:-3] if level > 1 else ''
                prefix = (' ' + symbol + '  ' if level > 1 else ' ') + prefix
            print (prefix + ('+-- ' if level > 0 else '') + word)
            first = False
        else:
            prefix = ('    ' * (level-1))
            prefix = (' ' + symbol + '  ' if level > 0 else '') + prefix
            print (prefix + ' +-- ' + word)
    return first
   
def buildTree(d, level = 0, skipPipe = False):
    stack = []
    start_index = 0
    first = True
    if '(' not in d:
        first = buildSub(d, level, first, skipPipe)
    else:
        for i in range(len(d)):
            if d[i] == '(':
                stack.append(i)
            elif d[i] == ')':
                if len(stack) == 0:
                    raise Exception('Invalid brackets')
                if len(stack) == 1:
                    first = buildSub(d[start_index:stack[0]], level, first, skipPipe)
                    # check if we see the last closing bracket == the last child
                    skipPipe = True if (level == 0 and i == len(d)-1) else skipPipe 
                    # strip is important to get rid of blanks between brackets
                    buildTree(d[stack[0] + 1:i].strip(), level + 1, skipPipe)
                    start_index = i + 1
                stack.pop()
 
d = "(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))"

buildTree(d, -1)