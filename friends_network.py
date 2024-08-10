import pandas as pd

friends_df = pd.DataFrame(columns=["friendA","friendB"]) # a global df for storing friends data

#adding new friendship for given two friends in bi-directional Eg: Alice->Bob, Bob->Alice
def add_friendship(friend1,friend2):
    global friends_df
    new_friendship = pd.DataFrame({"friendA":[friend1],"friendB":[friend2]}) 
    friends_df = pd.concat([friends_df,new_friendship],ignore_index=True)
    new_reverse = pd.DataFrame({"friendA":[friend2],"friendB":[friend1]})
    friends_df = pd.concat([friends_df,new_reverse],ignore_index=True)

#method for finding common friends for given two friends
def find_common_friends(friend1,friend2):
    common_friends1 = friends_df.loc[(friends_df["friendA"] == friend1)]["friendB"]
    common_friends2 = friends_df.loc[(friends_df["friendA"] == friend2)]["friendB"]
    common_friends = set(common_friends1).intersection(set(common_friends2))
    #print(f" COMMON FRIENDS {common_friends}")
    return common_friends
    
def nth_connection(friend1,friend2):
    if friend1 == friend2:
        return -1
    
    visited = set()
    queue = [(friend1,0)]  #friend and level
    
    while queue:
        current_friend,level = queue.pop(0)
        
        if current_friend in visited:
            continue
        visited.add(current_friend)
        
        friends_of_current_friend = friends_df.loc[friends_df["friendA"] == current_friend]["friendB"]
        for friend in friends_of_current_friend:
            if friend == friend2:
                return  level+1
            
            if friend not in visited:
                queue.append((friend,level+1))
    return -1

if __name__ == "__main__":
    
    add_friendship("Alice","Bob")
    add_friendship("Bob","Janice")
    add_friendship("Bob","Smith" )
    add_friendship("Alice","Smith")
    add_friendship("Alice", "Tom")
    add_friendship("Bob", "Tom")
    
    friend1 = "Alice"
    friend2 = "Bob"
    
    print(f'Common friends of {friend1} and {friend2} :{find_common_friends(friend1,friend2)}')
    
    friend1 = "Alice"
    friend2 = "Janice"
    print(f"Connection({friend1},{friend2})  :{nth_connection(friend1,friend2)}")