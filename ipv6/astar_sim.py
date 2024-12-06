from manimlib import *
from enum import Enum

COLOR_BACKGROUND = "#0A0C0A"

COLOR1 = '#010101'
COLOR2 = '#69779b'
# COLOR3 = BLUE_E
COLOR4 = '#f0ece2'
COLOR_GREEN_MARK = '#065535'
COLOR_RED_MARK = RED_E

# COLOR_CYAN = '#00FFC2'
# COLOR_GREEN = '#3DFF00'
# COLOR_YELLOW = '#FFC200'
# COLOR_RED = '#FF003D'
# COLOR_PURPLE = '#C200FF'
# COLOR_BLUE = '#003DFF'
COLOR_CYAN = '#00b58a'
COLOR_GREEN = '#2BB500'
COLOR_YELLOW = '#B58A00'
COLOR_RED = '#B5002B'
COLOR_PURPLE = '#8A00B5'
COLOR_BLUE = '#002BB5'
COLOR_GRAY = '#808080'

COLOR_CYAN_2 = '#00795c'
COLOR_GREEN_2 = '#1D7900'
COLOR_YELLOW_2 = '#795C00'
COLOR_RED_2 = '#79001D'
COLOR_PURPLE_2 = '#5C0079'
COLOR_BLUE_2 = '#001D79'

COLOR3 = COLOR_GREEN

COLOR_BLACK = "#0A0C0A"


class NodeStatus(Enum):
    OBSTACLE = -1
    OPEN     = 0
    VISITED  = 1 
    START    = 2
    GOAL     = 3
    PATH     = 4


class AStar2(Scene): 
    def setup(self):
        self.graph = None
        
        self.ndim = 8

        # self.box_amount = 4
        # self.box_width = 0.3

        self.box_amount = 16
        self.box_width = 0.3  # for 16

        # self.box_amount = 256
        # self.box_width = 0.025  # for 256

        self.box_stroke_width = 0.75
        
        self.ending_bits = 3 if self.box_amount == 16 else 3

        self.title = MarkupText(f"<u>A* Visualizer - IPv6</u>").set_color(COLOR4).scale(2.25)
        self.author = Text("CS 230 - Group 3").scale(0.5).move_to([3.95, -0.8, 0.0])

        self.source_address_container = ['A953', '006D', '0FAD', '0088', '000E', '0005', '878D', '6B51']
        # self.destin_address_container = ['A9F8', '002C', '0F79', '00DD', '00ED', '0004', '872E', '6BB6']  # for 256
        self.destin_address_container = ['A95E', '0061', '0FA1', '008A', '0002', '000C', '8781', '6B5B']  # for 16

        self.source_address_main = Text(':'.join(self.source_address_container)).scale(1.25).move_to([0.0, 1.5, 0.0]).set_color(COLOR_RED_2)
        self.destin_address_main = Text(':'.join(self.destin_address_container)).scale(1.25).move_to([0.0, -1.5, 0.0]).set_color(COLOR_BLUE_2)
        self.source_to_dest_arrow_main = Arrow(self.source_address_main, self.destin_address_main, thickness=2.5)
        self.source_address_main2 = Text(':'.join(self.source_address_container)).scale(1.25).move_to([0.0, 1.5, 0.0])
        self.destin_address_main2 = Text(':'.join(self.destin_address_container)).scale(1.25).move_to([0.0, -1.5, 0.0])
        self.source_label = Text("source").scale(0.3).move_to([-6.15, 0.55, 0.0]).set_color(COLOR_RED_2)
        self.destin_label = Text("destination").scale(0.3).move_to([-1.5, -0.95, 0.0]).set_color(COLOR_BLUE_2)
        self.source_address = Text(':'.join(self.source_address_container)).scale(0.55).move_to([-3.75, 0.75, 0.0]).set_color(COLOR_RED_2)
        self.destin_address = Text(':'.join(self.destin_address_container)).scale(0.55).move_to([-3.75, -0.75, 0.0]).set_color(COLOR_BLUE_2)
        self.source_address_main2.set_color_by_text_to_color_map({
            self.source_address_container[0]: COLOR_RED_2,
            self.source_address_container[1]: COLOR_RED_2,
            self.source_address_container[2]: COLOR_YELLOW_2,
            self.source_address_container[3]: COLOR_YELLOW_2,
            self.source_address_container[4]: COLOR_BLUE_2,
            self.source_address_container[5]: COLOR_BLUE_2,
            self.source_address_container[6]: COLOR_PURPLE_2,
            self.source_address_container[7]: COLOR_PURPLE_2
        })
        self.destin_address_main2.set_color_by_text_to_color_map({
            self.destin_address_container[0]: COLOR_RED_2,
            self.destin_address_container[1]: COLOR_RED_2,
            self.destin_address_container[2]: COLOR_YELLOW_2,
            self.destin_address_container[3]: COLOR_YELLOW_2,
            self.destin_address_container[4]: COLOR_BLUE_2,
            self.destin_address_container[5]: COLOR_BLUE_2,
            self.destin_address_container[6]: COLOR_PURPLE_2,
            self.destin_address_container[7]: COLOR_PURPLE_2
        })
        self.source_to_dest_arrow = Arrow(self.source_address, self.destin_address, thickness=2.5)

        self.source_group = [Text(f'g{idx}:g{idx+1}').scale(0.65).move_to([2.0, 2.95, 0.0]).set_color(COLOR_RED_2) for idx in range(1,self.ndim+1)]
        self.destin_group = [Text(f'g{idx}:g{idx+1}').scale(0.65).move_to([4.0, 2.95, 0.0]).set_color(COLOR_BLUE_2)  for idx in range(1,self.ndim+1)]
        self.sgroup_to_dgroup = [Arrow(self.source_group[idx], self.destin_group[idx], thickness=1.5) for idx in range(len(self.source_group))]
        self.source_group_last2 = [Text(f'{self.source_address_container[idx]}:{self.source_address_container[idx+1]}').scale(0.65).move_to([1.6, 2.55, 0.0]).set_color(COLOR_RED_2) \
                                   for idx in range(len(self.source_address_container)-1)]
        self.destin_group_last2 = [Text(f'{self.destin_address_container[idx]}:{self.destin_address_container[idx+1]}').scale(0.65).move_to([4.4, 2.55, 0.0]).set_color(COLOR_BLUE_2)  \
                                   for idx in range(len(self.destin_address_container)-1)]
        self.source_to_destin = [Arrow(self.source_group_last2[idx], self.destin_group_last2[idx], thickness=1.5) for idx in range(len(self.source_group_last2))]


        # self.start_idx = [0 for _ in range(self.ndim)]
        # self.desti_idx = [15 for _ in range(self.ndim)]
        # self.obstacles = [[5 for _ in range(self.ndim)], 
        #                   [4 for _ in range(self.ndim)], 
        #                   [9 for _ in range(self.ndim)]]
        self.start_idx = [int(group[self.ending_bits:], 16) for group in self.source_address_container]
        self.desti_idx = [int(group[self.ending_bits:], 16) for group in self.destin_address_container]

        self.obstacles = []
        self.obs_percent = 0.5

        # print(self.start_idx)
        # print(self.desti_idx)
        
        self.start_node = None
        self.desti_node = None

        self.graphs = []
        self.graph_objs = []
        self.graph_anims = []

    def construct(self):
        # self.play(ShowCreation(Line(UP, DOWN)))
        # self.play(ShowCreation(Line(RIGHT, LEFT)))
        self.play_title()
        self.initialize_graph()
        # self.initialize_nodes_ndim()
        # self.initialize_nodes()
        # self.run_astar()
        self.run_astar_ndim()
        self.cleanup()

    def play_title(self):
        self.play(
            AnimationGroup(
                Write(self.title), 
                Write(self.author),
                lag_ratio=0.5), run_time=2.0)
        self.wait()
        self.play(Uncreate(self.author, run_time=0.75))
        self.play(self.title.animate.scale(0.4).to_edge(UL))
        self.wait()
        
    def initialize_graph(self):
        # self.play(ShowCreation(self.source_address))
        # self.play(ShowCreation(self.destin_address))
        start_pos = [3.0, -0.5, 0.0]
        self.graph = NDimGraph(self,    
                               dimensions = [self.box_amount for _ in range(self.ndim)])
        self.graph1 = TwoDimGraph(self,
                                  x_label = 'g1',
                                  y_label = 'g2',
                                  dimensions = [self.box_amount,self.box_amount],
                                  start_pos = start_pos,
                                  stroke_width = self.box_stroke_width,
                                  box_size = self.box_width)
        self.graph2 = TwoDimGraph(self,
                                  x_label = 'g3',
                                  y_label = 'g4',
                                  dimensions = [self.box_amount,self.box_amount],
                                  start_pos = start_pos,
                                  stroke_width = self.box_stroke_width,
                                  box_size = self.box_width)
        self.graph3 = TwoDimGraph(self,
                                  x_label = 'g5',
                                  y_label = 'g6',
                                  dimensions = [self.box_amount,self.box_amount],
                                  start_pos = start_pos,
                                  stroke_width = self.box_stroke_width,
                                  box_size = self.box_width)    
        self.graph4 = TwoDimGraph(self,
                                  x_label = 'g7',
                                  y_label = 'g8',
                                  dimensions = [self.box_amount,self.box_amount],
                                  start_pos = start_pos,
                                  stroke_width = self.box_stroke_width,
                                  box_size = self.box_width)
        # self.graph5 = TwoDimGraph(self,
        #                           x_label = 'g5',
        #                           y_label = 'g6',
        #                           dimensions = [self.box_amount,self.box_amount],
        #                           start_pos = [0.0, 0.0, 0.0],
        #                           stroke_width = self.box_stroke_width,
        #                           box_size = self.box_width)
        # self.graph6 = TwoDimGraph(self,
        #                           x_label = 'g6',
        #                           y_label = 'g7',
        #                           dimensions = [self.box_amount,self.box_amount],
        #                           start_pos = [0.0, 0.0, 0.0],
        #                           stroke_width = self.box_stroke_width,
        #                           box_size = self.box_width)
        # self.graph7 = TwoDimGraph(self,
        #                           x_label = 'g7',
        #                           y_label = 'g8',
        #                           dimensions = [self.box_amount,self.box_amount],
        #                           start_pos = [0.0, 0.0, 0.0],
        #                           stroke_width = self.box_stroke_width,
        #                           box_size = self.box_width) 
        
        self.graph_anims.append(self.graph1.construct(play=False))
        self.graph_anims.append(self.graph2.construct(play=False))
        self.graph_anims.append(self.graph3.construct(play=False))
        self.graph_anims.append(self.graph4.construct(play=False))
        # self.graph_anims.append(self.graph5.construct(play=False))
        # self.graph_anims.append(self.graph6.construct(play=False))
        # self.graph_anims.append(self.graph7.construct(play=False))

        self.graphs = [self.graph1,
                       self.graph2,
                       self.graph3,
                       self.graph4,]
                    #    self.graph5,
                    #    self.graph6,
                    #    self.graph7]

        self.graph_borders = [RoundedRectangle(width=6, height=7.25, stroke_width = 0.5, color=WHITE).move_to([2.85,0.0,0.0]),
                              RoundedRectangle(width=6, height=7.25, stroke_width = 0.5, color=WHITE).move_to([2.85,0.0,0.0]),
                              RoundedRectangle(width=6, height=7.25, stroke_width = 0.5, color=WHITE).move_to([2.85,0.0,0.0]),
                              RoundedRectangle(width=6, height=7.25, stroke_width = 0.5, color=WHITE).move_to([2.85,0.0,0.0])]

        self.graph_objs +=    [VGroup(self.graphs[0].get_objs(), self.source_group[0], self.destin_group[0],
                                      self.source_group_last2[0], self.destin_group_last2[0],
                                      self.sgroup_to_dgroup[0], self.source_to_destin[0],
                                      self.graph_borders[0]),
                               VGroup(self.graphs[1].get_objs(), self.source_group[2], self.destin_group[2],
                                      self.source_group_last2[2], self.destin_group_last2[2],
                                      self.sgroup_to_dgroup[1], self.source_to_destin[1],
                                      self.graph_borders[1]),
                               VGroup(self.graphs[2].get_objs(), self.source_group[4], self.destin_group[4],
                                      self.source_group_last2[4], self.destin_group_last2[4],
                                      self.sgroup_to_dgroup[2], self.source_to_destin[2],
                                      self.graph_borders[2]),
                               VGroup(self.graphs[3].get_objs(), self.source_group[6], self.destin_group[6],
                                      self.source_group_last2[6], self.destin_group_last2[6],
                                      self.sgroup_to_dgroup[3], self.source_to_destin[3],
                                      self.graph_borders[3])]

    def initialize_nodes(self):
        self.start_node = self.graph.get_node(self.start_idx)
        self.start_node.set_status(NodeStatus.START)
        self.desti_node = self.graph.get_node(self.desti_idx)
        self.desti_node.set_status(NodeStatus.GOAL)

    def initialize_nodes_ndim(self, idx):
        # subnode = self.graphs[0].get_node([self.start_idx[0], self.start_idx[1]])
        # subnode.set_status(NodeStatus.START)
        # subnode = self.graphs[0].get_node([self.desti_idx[0], self.desti_idx[1]])
        # subnode.set_status(NodeStatus.GOAL)
        # for idx in range(1,self.ndim-1):
        #     subnode = self.graphs[idx].get_node([self.desti_idx[idx], self.start_idx[idx+1]])
        #     subnode.set_status(NodeStatus.START)
        #     subnode = self.graphs[idx].get_node([self.desti_idx[idx], self.desti_idx[idx+1]])
        #     subnode.set_status(NodeStatus.GOAL)
        subnode = self.graphs[idx//2].get_node([self.start_idx[idx], self.start_idx[idx+1]])
        subnode.set_status(NodeStatus.START)
        subnode = self.graphs[idx//2].get_node([self.desti_idx[idx], self.desti_idx[idx+1]])
        subnode.set_status(NodeStatus.GOAL)

        count = 0
        while count < self.box_amount**2 * self.obs_percent:
            coords = [random.randint(0,15), random.randint(0,15)]

            if self.graphs[idx//2].get_node(coords).get_status() in [NodeStatus.START, NodeStatus.GOAL, NodeStatus.OBSTACLE]:
                continue
            
            self.graphs[idx//2].get_node(coords).set_status(NodeStatus.OBSTACLE)
            count += 1

        # for idx in range(1,self.ndim-1):
        #     subnode = self.graphs[idx].get_node([self.desti_idx[idx], self.start_idx[idx+1]])
        #     subnode.set_status(NodeStatus.START)
        #     subnode = self.graphs[idx].get_node([self.desti_idx[idx], self.desti_idx[idx+1]])
        #     subnode.set_status(NodeStatus.GOAL)

    def run_astar_ndim(self):
        import heapq

        # start = [0,0,0,0,0,0,0,0]
        # 1st   = [16,16,0,0,0,0,0,0]       - [0,0]  -> [16,16]
        # 2nd   = [16,16,16,0,0,0,0,0]      - [16,0] -> [16,16]
        # ....
        # end   = [16,16,16,16,16,16,16,16] - [16,0] -> [16,16]

        def heuristic(start, end):
            p1, p2 = start.get_index(), end.get_index()
            return sum([abs(p1[idx]-p2[idx]) for idx in range(len(p1))])
        
        def get_directions(dim=2):
            directions = []
            for d in range(dim):
                temp = [0 for _ in range(dim)]
                temp[d] += 1
                directions.append(tuple(temp))
                temp[d] -= 2
                directions.append(tuple(temp))
            return directions
        
        self.play(FadeIn(self.source_address_main, shift=DOWN),
                  FadeIn(self.destin_address_main, shift=UP),
                  ShowCreation(self.source_to_dest_arrow_main))
        self.wait()

        self.play(Transform(self.source_address_main, self.source_address_main2),
                  Transform(self.destin_address_main, self.destin_address_main2))
        self.wait()

        self.play(Transform(self.source_address_main, self.source_address),
                  Transform(self.destin_address_main, self.destin_address),
                  Transform(self.source_to_dest_arrow_main, self.source_to_dest_arrow),
                  FadeIn(self.source_label, shift=DOWN),
                  FadeIn(self.destin_label, shift=DOWN))       

        self.wait()

        # for idx in range(self.ndim-1):
        for idx in range(0,self.ndim-1,2):
            # self.play(AnimationGroup(*self.graph_anims[idx//2]))
            # self.play(Write(self.source_group[idx]),
            #           Write(self.destin_group[idx]),
            #           Write(self.sgroup_to_dgroup[idx]),
            #           Write(self.source_group_last2[idx]),
            #           Write(self.destin_group_last2[idx]),
            #           Write(self.source_to_destin[idx]))
            self.play(FadeIn(self.graph_objs[idx//2], shift=UP*1.5))
            self.initialize_nodes_ndim(idx)
            self.wait()

            start_subnode_idx = [self.start_idx[idx], self.start_idx[idx+1]]
            desti_subnode_idx = [self.desti_idx[idx], self.desti_idx[idx+1]]

            start_subnode = self.graphs[idx//2].get_node(start_subnode_idx)
            desti_subnode = self.graphs[idx//2].get_node(desti_subnode_idx)

            open_set = []
            heapq.heappush(open_set, (0, start_subnode))

            came_from = {}
            
            g_score = {start_subnode: 0}  # Cost from start to each node
            f_score = {start_subnode: heuristic(start_subnode, desti_subnode)}  # Estimated total cost

            directions = get_directions(dim=2)

            cost = 0
            while open_set:
                _, current = heapq.heappop(open_set)
                # print(current.get_index())

                if current.get_status() == NodeStatus.GOAL:
                    path = []
                    while current in came_from:
                        path.append(current)
                        cost += current.get_weight()
                        current = came_from[current]
                        if current.get_status() != NodeStatus.START: current.set_status(NodeStatus.PATH)
                    path.append(self.start_node)
                    break

                if current.get_status() != NodeStatus.START: current.set_status(NodeStatus.VISITED)
        
                for d in directions:
                    # cur_idx = current.get_index()
                    neighbor = self.graphs[idx//2].get_node([current.get_index()[0] + d[0], current.get_index()[1] + d[1]])
                    # neighbor = self.graphs[idx].get_node([cur_idx[idx] + d[idx] for idx in range(len(d))])

                    # if neighbor and neighbor.get_status() != NodeStatus.OBSTACLE:
                    if neighbor:
                        tent_g_score = g_score[current] + 1

                        if neighbor not in g_score or tent_g_score < g_score[neighbor]:
                            came_from[neighbor] = current
                            g_score[neighbor] = tent_g_score + neighbor.get_weight()
                            f_score[neighbor] = tent_g_score + heuristic(neighbor, desti_subnode)
                            heapq.heappush(open_set, (f_score[neighbor], neighbor))

            cost_text = Text(f"Total Cost: {cost}", stroke_color=COLOR_GREEN).scale(0.7).move_to([3.0, -3.0, 0.0])
            self.graph_objs[idx//2].add(cost_text)
            self.play(Write(cost_text))

            self.wait()
            self.play(FadeOut(self.graph_objs[idx//2],shift=UP*1.5))
            # self.play(Uncreate(cost_text),
            #           Uncreate(self.source_group[idx]),
            #           Uncreate(self.destin_group[idx]),
            #           Uncreate(self.sgroup_to_dgroup[idx]),
            #           Uncreate(self.source_group_last2[idx]),
            #           Uncreate(self.destin_group_last2[idx]),
            #           Uncreate(self.source_to_destin[idx]),
            #           run_time=0.5)
            # self.graphs[idx//2].cleanup()
        
        self.play(Uncreate(self.source_address),
                  Uncreate(self.destin_address),
                  Uncreate(self.source_label),
                  Uncreate(self.destin_label),
                  Uncreate(self.source_to_dest_arrow))

    # def run_astar(self):
    #     import heapq

    #     def heuristic(start, end):
    #         p1, p2 = start.get_index(), end.get_index()
    #         return sum([abs(p1[idx]-p2[idx]) for idx in range(len(p1))])
        
    #     def get_directions(dim=2):
    #         directions = []
    #         for d in range(dim):
    #             temp = [0 for _ in range(dim)]
    #             temp[d] += 1
    #             directions.append(tuple(temp))
    #             temp[d] -= 2
    #             directions.append(tuple(temp))
    #         return directions

    #     open_set = []
    #     heapq.heappush(open_set, (0, self.start_node))
        
    #     came_from = {}
    #     g_score = {self.start_node: 0}  # Cost from start to each node
    #     f_score = {self.start_node: heuristic(self.start_node, self.desti_node)}  # Estimated total cost

    #     directions = get_directions(dim=self.ndim)

    #     while open_set:
    #         _, current = heapq.heappop(open_set)
            
    #         if current.get_status() == NodeStatus.GOAL:
    #             path = []
    #             while current in came_from:
    #                 path.append(current)
    #                 current = came_from[current]
    #                 if current.get_status() != NodeStatus.START: current.set_status(NodeStatus.PATH)
    #             path.append(self.start_node)
    #             break
            
    #         if current.get_status() != NodeStatus.START: current.set_status(NodeStatus.VISITED)
        
    #         for d in directions:
    #             cur_idx = current.get_index()
    #             # neighbor = self.graph.get_node([current.get_index()[0] + d[0], current.get_index()[1] + d[1]])
    #             neighbor = self.graph.get_node([cur_idx[idx] + d[idx] for idx in range(len(d))])

    #             if neighbor and neighbor.get_status() != NodeStatus.OBSTACLE:
    #                 tent_g_score = g_score[current] + 1

    #                 if neighbor not in g_score or tent_g_score < g_score[neighbor]:
    #                     came_from[neighbor] = current
    #                     g_score[neighbor] = tent_g_score
    #                     f_score[neighbor] = tent_g_score + heuristic(neighbor, self.desti_node)
    #                     heapq.heappush(open_set, (f_score[neighbor], neighbor))

    def cleanup(self,
                play: bool = True):
        cleanup_anims = []

        # if self.source_address: cleanup_anims.append(Uncreate(self.source_address))
        # if self.destin_address: cleanup_anims.append(Uncreate(self.destin_address))

        # if self.graph1: cleanup_anims += self.graph1.cleanup(play=False)
        # if self.graph2: cleanup_anims += self.graph2.cleanup(play=False)
        # if self.graph3: cleanup_anims += self.graph3.cleanup(play=False)
        # if self.graph4: cleanup_anims += self.graph4.cleanup(play=False)
        # if self.graph5: cleanup_anims += self.graph5.cleanup(play=False)
        # if self.graph6: cleanup_anims += self.graph6.cleanup(play=False)
        # if self.graph7: cleanup_anims += self.graph7.cleanup(play=False)

        if self.title: cleanup_anims.append(Uncreate(self.title))
        if self.author: cleanup_anims.append(Uncreate(self.author))

        if play and cleanup_anims:
            self.play(AnimationGroup(*cleanup_anims))
        return cleanup_anims


class NDimGraph():
    def __init__(self,
                 scene: Scene,
                 ndim: int = 2,
                 dimensions: list[int] = [256, 256]):
        self.scene = scene

        self.ndim = ndim
        self.dimensions = dimensions

    def get_node(self,
                 index: list[int]):
        return self.graph[index[0]][index[1]] if 0 <= index[0] < self.dimensions[0] and 0 <= index[1] < self.dimensions[1] else None


class TwoDimGraph():
    def __init__(self,
                 scene: Scene,
                 x_label: str = 'x',
                 y_label: str = 'y',
                 dimensions: list[int] = [256, 256],
                 start_pos: list[float] = [0.0, 0.0, 0.0],
                 stroke_color = WHITE,
                 stroke_width = 2.0,
                 box_size = 1.0):
        self.scene = scene

        self.dimensions = dimensions
        self.start_x = start_pos[0] - box_size*(dimensions[0]/2)
        self.start_y = start_pos[1] + box_size*(dimensions[1]/2)
        self.x, self.y, self.z = start_pos[0] - box_size*(dimensions[0]/2), start_pos[1] + box_size*(dimensions[1]/2), start_pos[2]

        self.x_label = Text(f"{x_label}").scale(0.4).move_to([self.start_x - 0.25,                    self.start_y - box_size*dimensions[1] - 0.1, start_pos[2]])
        self.y_label = Text(f"{y_label}").scale(0.4).move_to([self.start_x + box_size*dimensions[0], self.start_y + 0.295,                          start_pos[2]])

        self.origin_label = Text(f"0x00").scale(0.5).move_to([self.start_x-0.275,                      self.start_y + 0.295,                          start_pos[2]])
        self.end_label    = Text(f"0xFF").scale(0.5).move_to([self.start_x + box_size*dimensions[0], self.start_y - box_size*dimensions[1] - 0.1, start_pos[2]])

        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.box_size = box_size

        self.objs = VGroup(self.x_label, self.y_label,
                           self.origin_label, self.end_label)
        self.graph = []

        self.init_anim = []

    def get_objs(self):
        return self.objs

    def get_node(self,
                 index: list[int]):
        return self.graph[index[0]][index[1]] if 0 <= index[0] < self.dimensions[0] and 0 <= index[1] < self.dimensions[1] else None

    def construct(self,
                  play = False):
        for idx in range(self.dimensions[0]):
            row = []
            for jdx in range(self.dimensions[1]):
                sq = self.construct_box(idx, jdx)
                self.update_pos_horiz()
                row.append(sq)
            self.update_pos_verti()
            self.x = self.start_x
            self.graph.append(row)

        self.init_anim.append(Write(self.x_label))
        self.init_anim.append(Write(self.y_label))
        self.init_anim.append(Write(self.origin_label))
        self.init_anim.append(Write(self.end_label))
        
        if play: self.scene.play(AnimationGroup(*self.init_anim))
        
        return self.init_anim

    def construct_box(self, rowidx, coljdx):
        node = Node(scene = self.scene,
                    pos = [self.x, self.y, self.z],
                    index = [rowidx, coljdx],
                    side_length = self.box_size,
                    stroke_color = self.stroke_color,
                    stroke_width = self.stroke_width,
                    content_color = COLOR_BLACK)
        # print([rowidx, coljdx])
        self.objs.add(node.get_obj())
        self.init_anim.append(node.construct(play=False))
        return node
    
    def update_pos_horiz(self):
        self.x += self.box_size

    def update_pos_verti(self):
        self.y -= self.box_size

    def cleanup(self,
                play: bool = True):
        cleanup_anims = []

        # if self.objs: cleanup_anims.append(Uncreate(self.objs, run_time=0.5))
        if self.graph:
            for row in self.graph:
                for node in row:
                    cleanup_anims += node.cleanup(play=False)

        if self.x_label: cleanup_anims.append(Uncreate(self.x_label))
        if self.y_label: cleanup_anims.append(Uncreate(self.y_label))
        if self.origin_label: cleanup_anims.append(Uncreate(self.origin_label))
        if self.end_label:    cleanup_anims.append(Uncreate(self.end_label))

        if play: self.scene.play(AnimationGroup(*cleanup_anims))
        return cleanup_anims
    

class Node():
    def __init__(self,
                 scene:         Scene,
                 pos:           list[float] = [0.0, 0.0, 0.0],
                 index:         list[int]   = [0, 0, 0],
                 side_length:   float       = 1.0,
                 stroke_color:  str         = WHITE,
                 stroke_width:  float       = 2.0,
                 content_color: str         = COLOR_BLACK,
                 opacity:       float       = 0.5,
                 run_time:      float       = 0.25):
        self.scene = scene

        self.pos   = pos
        self.index = index
        self.weight = 0

        self.status = NodeStatus.OPEN

        self.side_length   = side_length
        self.stroke_color  = stroke_color
        self.stroke_width  = stroke_width
        self.content_color = content_color
        self.opacity       = opacity
        self.run_time      = run_time

        self.box = None
        self.label = None

        self.node = VGroup()

        self.status_color = {NodeStatus.OBSTACLE: COLOR_GRAY,
                             NodeStatus.OPEN    : COLOR_BACKGROUND,
                             NodeStatus.VISITED : COLOR_YELLOW,
                             NodeStatus.START   : COLOR_RED,
                             NodeStatus.GOAL    : COLOR_BLUE,
                             NodeStatus.PATH    : COLOR_GREEN}

    def __lt__(self, other):
        return True
    
    def __gt__(self, other):
        return True
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.index == other.index
    
    def __hash__(self):
        return hash(tuple(self.index))
    
    def get_obj(self):
        return self.node

    def get_pos(self):
        return self.pos
    
    def get_index(self):
        return self.index 
    
    def get_node(self):
        return self.node
    
    def get_status(self):
        return self.status
    
    def get_weight(self):
        return self.weight
    
    def set_status(self,
                   newstatus: NodeStatus = NodeStatus.OPEN):
        self.status = newstatus
        self.set_color(self.status) 
    
    def set_color(self, 
                  status = None,
                  color = None):
        self.content_color = color if color else self.status_color[status]
        if self.status == NodeStatus.START:
            self.weight = 0
            self.label = Text('S').scale(0.25).move_to(self.box)
        elif self.status == NodeStatus.GOAL:
            self.weight = 0
            self.label = Text('D').scale(0.25).move_to(self.box)
        elif self.status == NodeStatus.OBSTACLE:
            self.weight = random.randint(1,10)
            self.label = Text(f"{self.weight}").scale(0.25).move_to(self.box)
        # elif self.status not in [NodeStatus.START, NodeStatus.GOAL, NodeStatus.OBSTACLE] and self.label:
        #     self.weight = 0
        #     self.scene.play(Uncreate(self.label)) 
        #     self.label = None
        # self.box.set_fill(color=self.content_color, opacity=self.opacity)
        self.scene.play(self.box.animate.set_fill(self.content_color, opacity=self.opacity),
                        run_time = 0.25 if self.status in [NodeStatus.START, NodeStatus.GOAL] else 0.005)
        if self.label: 
            self.scene.play(Write(self.label, run_time=0.5 if self.weight == 0 else 0.005)) 
            self.node.add(self.label)
    
    def construct(self,
                  play = False):
        self.box = Square(side_length=self.side_length, 
                          color=self.stroke_color, 
                          stroke_width=self.stroke_width)
        self.box.move_to(self.pos)
        self.node.add(self.box)
        if play: self.scene.play(ShowCreation(self.box, run_time=self.run_time))
        return ShowCreation(self.box, run_time=self.run_time)

    def cleanup(self,
                play: bool = True):
        cleanup_anims = []

        if self.node: cleanup_anims.append(Uncreate(self.node, run_time=0.5))

        if self.label: cleanup_anims.append(Uncreate(self.label, run_time=0.5))

        if play:
            self.scene.play(AnimationGroup(*cleanup_anims))
        return cleanup_anims
    
