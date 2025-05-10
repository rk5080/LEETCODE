class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def findUPar(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


class Solution(object):
    def accountsMerge(self, details):
        n = len(details)
        dsu = DisjointSet(n)
        mail_to_node = {}

        # Step 1: Map each email to its user and union users with shared emails
        for i in range(n):
            for email in details[i][1:]:
                if email not in mail_to_node:
                    mail_to_node[email] = i
                else:
                    dsu.unionBySize(i, mail_to_node[email])

        # Step 2: Create merged mail list based on DSU parent
        merged_mail = [[] for _ in range(n)]
        for email, node in mail_to_node.items():
            root = dsu.findUPar(node)
            merged_mail[root].append(email)

        # Step 3: Construct the final merged account list
        ans = []
        for i in range(n):
            if merged_mail[i]:
                merged_mail[i].sort()
                name = details[i][0]
                merged_account = [name] + merged_mail[i]
                ans.append(merged_account)

        return ans