class Team:
    def __init__(self, input_name, input_list_of_players, input_coach):
        self.name = input_name
        self.players = input_list_of_players
        self.coach = input_coach
        self.points = 0


    def add_player(self, input_new_player):
        self.players.append(input_new_player) 

    def has_player(self, input_check_player):
        # if input_check_player in self.players:
        #     return True
        # else:
        #     return False

    # # or
        return input_check_player in self.players 
    # or 

    # def has_player(self, input_check_player):
    #     return self.players.count(input_check_player > 0)
        
    def play_game(self, input_True_or_False):
        if input_True_or_False:
            self.points += 3
        
        


        
    
        
    
    