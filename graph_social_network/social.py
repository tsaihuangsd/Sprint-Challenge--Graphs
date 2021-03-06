import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # print error if trying to create less than 1 user
        if numUsers < 1:
            print("Must create at least one user")
            return None
        
        # create users
        for id in range(0, numUsers):
            self.users[id] = User("User" + str(id))
        
        # establish number of friendship per user
        user_list = self.users.values()

        # for user in user_list:
        #     print(user.name)
        
        for id in range(1, int(len(user_list)/2)+1 ):
            max_num_friendship = avgFriendships*2
            num_friendship = random.randint(0, max_num_friendship)
            self.friendships[id*2-1] = num_friendship
            self.friendships[id*2] = max_num_friendship - num_friendship
        #     print((self.friendships[id*2-1], self.friendships[id*2]))
        # print(self.friendships)

        establish frienship between users
        for friendship in self.friendships:
            print(friendship)


            # if user not in visited:
            #     rest_of_users = del dict(self.users)[user]
            #     max_num_friendship+1)
            #     self.friendships[id]

            # visited.append(user)

        


        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
