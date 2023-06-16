from manim import *
class UpdateSin(Scene):
    CONFIG={
        'rate':[TAU/2,TAU/4,TAU/8,TAU/16],
        't_offset':[1,2,3,4],
    }
    def construct(self):
        def update_curve(c,dt):
            rate=dt
            c.become(self.get_sin_graph(c.dx))
            c.dx+=rate
        curves=VGroup()
        for i in range(len(self.CONFIG['rate'])):
            curve=self.get_sin_graph(self.CONFIG['t_offset'][i]+self.CONFIG['rate'][i])
            curve.dx=self.CONFIG['t_offset'][i]+self.CONFIG['rate'][i]
            curve.add_updater(update_curve)
            curves.add(curve)
        self.add(curves)
        self.wait(4)
    def get_sin_graph(self,dx):
        graph=FunctionGraph(
            lambda x: 3*np.sin(x+dx),
        )
        graph.dx=dx
        return graph