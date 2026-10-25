class Graf:
    def __init__(self, orientovany=False):
        self.orientovany = orientovany
        self.adj = {}
        self.ohodnoceny = False

    def pridej_uzel(self, u):
        if u not in self.adj:
            self.adj[u] = {}

    def pridej_hranu(self, u, v, vaha=None):
        self.pridej_uzel(u)
        self.pridej_uzel(v)
        if vaha is not None:
            self.ohodnoceny = True
        self.adj[u][v] = vaha
        if not self.orientovany:
            self.adj[v][u] = vaha

    def analyza(self):
        hrany = set()
        for u in self.adj:
            for v in self.adj[u]:
                if self.orientovany:
                    hrany.add((u, v))
                else:
                    hrany.add(tuple(sorted([u, v])))

        uzly_pocet = len(self.adj)
        hrany_pocet = len(hrany)

        smycky = any(u in self.adj[u] for u in self.adj)
        planarne = hrany_pocet <= 3 * uzly_pocet - 6 if uzly_pocet >= 3 else True

        print(f"Pocet uzlu: {uzly_pocet}")
        print(f"Pocet hran: {hrany_pocet}")
        print(f"Orientovany: {self.orientovany}")
        print(f"Ohodnoceny: {self.ohodnoceny}")
        print(f"Obsahuje smycky: {smycky}")
        print(f"Planarni odhad: {planarne}")


if __name__ == "__main__":
    g = Graf()
    g.pridej_hranu("A", "B", 5)
    g.pridej_hranu("B", "C")
    g.pridej_hranu("C", "A")
    g.pridej_hranu("C", "D")
    
    g.analyza()
