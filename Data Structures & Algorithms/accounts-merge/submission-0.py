class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node: int) -> int:
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        
        if pu == pv:
            return False
        
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # accounts[i] = list of strings
        # accounts[i][0] = name | rest are emails

        # two accounts belong to same person if common email to both accounts
        # same name doesn't mean same person
        # person can have multiple accs but they all have the same name

        # return accounts: [name, emails_sorted...]
        # accounts can be in any order (by name etc)

        # 1. for any two lists to be merged, they must have the same name as a first step
        # 2. does any email in the account match any email under an identical name account
        # 3. if yes, merge all emails into one account, otherwise keep accounts seperate
        # 4. .sort() or sorted() the emails per account

        # this looks like a graph problem with associations and traversal that can be
        # similar to dfs or bfs and a visited set perhaps.

        # my approach: traverse the accounts 2d arr, and look at the first element of each
        # to get the name, 
        
        n = len(accounts)
        dsu = DSU(n)

        emailToIndx = {} # {email: accIndex}
        for indx, acc in enumerate(accounts): # for every acc
            for email in acc[1:]:
                if email in emailToIndx:
                    dsu.union(indx, emailToIndx[email])
                else:
                    emailToIndx[email] = indx
        
        parentToEmails = defaultdict(list) # (parentIndx: mergedEmails)
        for email, indx in emailToIndx.items():
            parent = dsu.find(indx)
            parentToEmails[parent].append(email)
        
        res = []
        for indx, emails in parentToEmails.items():
            name = accounts[indx][0]
            res.append([name] + sorted(emails)) # dont forget to sort emails
        return res


