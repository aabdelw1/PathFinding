import visgraph
import Tkinter as tk
import pprint
from shapely.geometry import Point, Polygon

def main2():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500, 
                       highlightthickness=0, bg="white")
    canvas.pack()
    obstacles = [
        [
            (125, 125),
            (225, 125),
            (225, 175),
            (125, 175)
        ],
    ]
    obstacles = [
        [
            (320, 200),
            (280, 230),
            (220, 230),
            (180, 200),
            (220, 170),
            (280, 170)
        ],
        [
            (225, 175),
            (265, 225),
            (225, 275)
        ],
        [
            (125, 125),
            (225, 125),
            (225, 175),
            (125, 175)
        ],
        [
            (375, 25),
            (475, 25),
            (475, 100),
            (425, 160),
            (375, 100)
        ]
    ]
    fly_zone = [
        (10, 10),
        (10, 490),
        (490, 490),
        (490, 10)
    ]
    waypt = (450, 450, 20)
    graph = visgraph.VisibilityGraph(obstacles, 10, fly_zone)
    path = graph.find_path((30, 30), waypt)
    pprint.PrettyPrinter(indent=2).pprint(path)
    draw_graph(graph, canvas)
    draw_path(path, canvas)
    draw_poly(Point(waypt[0], waypt[1]).buffer(waypt[2]), canvas, "purple", outline=True)
    root.mainloop()

def draw_path(path, canvas):
    for i in range(len(path)-1):
        x, y = path[i]
        x2, y2 = path[i+1]
        canvas.create_line(x, y, x2, y2, fill="purple")

def draw_graph(graph, canvas):
    draw_poly(Polygon([(0, 0), (500, 0), (500, 500), (0, 500)]), canvas, "blue")
    draw_poly(graph.fly_zone, canvas, "white")
    for obstacle in graph.obstacles:
        draw_poly(obstacle, canvas, "blue")
    for n in graph.nodes:
        canvas.create_oval(n.x-n.r, n.y-n.r, n.x+n.r, n.y+n.r, outline="green")

def draw_grid(grid, canvas):
    for obstacle in grid.obstacles:
        draw_poly(obstacle, canvas, "blue")
    for col in grid.nodes:
        for node in col:
            if not node.occupied:
                draw_poly(node.poly, canvas, "green", outline=True)
    for col in grid.nodes:
        for node in col:
            if node.occupied:
                draw_poly(node.poly, canvas, "red", outline=True)

def draw_poly(poly, canvas, color, outline=False):
    if outline:
        vertices = list(poly.exterior.coords)
        for i in range(len(vertices)-1):
            cur = vertices[i]
            nxt = vertices[i+1]
            canvas.create_line(cur[0], cur[1], nxt[0], nxt[1], fill=color)
    else:
        flat_verts = []
        for v in list(poly.exterior.coords):
            flat_verts += [v[0], v[1]]
        canvas.create_polygon(*flat_verts, fill=color)

if __name__ == '__main__':
    main2()
