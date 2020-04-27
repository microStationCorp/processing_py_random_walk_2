stack = []
covered = []
direction = [[4, 0], [-4, 0], [0, 4], [0, -4]]
pos = []
r = 255
g = 0
b = 0
cobj = {
    'r': 'h',
    'g': 'i',
    'b': 'h'
}

def setup():
    global pos, r, g, b
    size(400, 400)
    background(0)
    strokeWeight(4)
    pos = [0, 0]
    stack.append(pos)
    covered.append(pos)
    stroke(r, g, b)
    point(pos[0], pos[1])

def draw():
    global stack, covered, r, g, b, cobj
    if len(stack) != 0:
        crnt = stack[len(stack) - 1]
        adj = get_adj(crnt)
        if adj != None:
            stack.append(adj)
            covered.append(adj)
            stroke(r, g, b)
            point(adj[0], adj[1])
            if cobj['r'] == 'i':
                if r < 255:
                    r += 1
                else:
                    cobj['r'] = 'h'
                    cobj['b'] = 'd'
            elif cobj['r'] == 'd':
                if r > 0:
                    r -= 1
                else:
                    cobj['r'] = 'h'
                    cobj['b'] = 'i'
            elif cobj['g'] == 'i':
                if g < 255:
                    g += 1
                else:
                    cobj['r'] = 'd'
                    cobj['g'] = 'h'
            elif cobj['g'] == 'd':
                if g > 0:
                    g -= 1
                else:
                    cobj['g'] = 'h'
                    cobj['r'] = 'i'
            elif cobj['b'] == 'i':
                if b < 255:
                    b += 1
                else:
                    cobj['b'] = 'h'
                    cobj['g'] = 'd'
            elif cobj['b'] == 'd':
                if b > 0:
                    b -= 1
                else:
                    cobj['b'] = 'h'
                    cobj['g'] = 'i'
        else:
            stack.pop()


def get_adj(current):
    global direction, covered
    adj = []
    for dir in direction:
        x = current[0] + dir[0]
        y = current[1] + dir[1]

        if x >= 0 and y >= 0 and x <= width and y <= height and [x, y] not in covered:
            adj.append([x, y])
    if len(adj) != 0:
        return adj[int(random(len(adj)))]
    else:
        return None
