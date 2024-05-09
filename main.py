# This file is for strategy


from util.objects import *
from util.routines import *
from util.tools import find_hits

class Bot(GoslingAgent):
    #This function runs every in-game tick
    def run(self):
        if self.get_intent() is not None:
           if self.time % 3 == 0:
               print('no intent')
           return
        if self.kickoff_flag:
            print('kicking off')
            self.set_intent(kickoff())
            return
        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post)
        }
        opponent_location = self.foes[0].location
        hits = find_hits(self, targets)



        opponent_distance_from_ball = (self.foes[0].location - self.ball.location).magnitude()
        our_distance_from_ball = (self.me.location - self.ball.location).magnitude()
        oppenent_closer_to_ball = (opponent_distance_from_ball < our_distance_from_ball)
        we_closer_to_ball = (opponent_distance_from_ball > our_distance_from_ball)

        if self.is_ball_infront_of_us():
            print('The ball is infront of us, thus, this statement is true')
        else:
            print('The ball is behind us')

        if we_closer_to_ball:
            if len(hits['at_opponent_goal']) > 0:
                #attacking
                self.set_intent(hits['at_opponent_goal'][0])
                print('Attacking!')
                return
        

        if len(hits['away_from_our_net']) > 0:
            self.set_intent(hits['away_from_our_net'][0])
            print('hitting our post')
            return


        if self.me.boost == 100:
            self.set_intent(short_shot(self.foe_goal.location))
            return
        


        if self.is_in_front_of_ball():
            #defending strat
            print('using defending strat')
            self.set_intent(goto(self.friend_goal.location))
            return
        
        if self.is_ball_infront_of_us():
            print('The ball is infront of us, thus, this statement is true')
        

        if oppenent_closer_to_ball:
            self.set_intent(goto(self.friend_goal.location))
            



        

        closest_boost = self.get_closest_large_boost()
        if closest_boost is not None:
            print('geting boost')
            self.set_intent(goto(closest_boost.location))
            return
        
        if self.me.boost < 5 and self.get_intent != 'Attacking!':
            print('good question')
            return
        














#class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    # def run(self):
    #     d1 = abs(self.me.location.y - self.foe_goal.location.y)
    #     d2 = abs(self.ball.location.y - self.foe_goal.location.y)
    #     is_infront_of_ball = d1 > d2
    #     if self.kickoff_flag:
    #         is_in_front_of_ball = False
    #         #The line below tells the bot what it's trying to do
    #         self.set_intent(kickoff())
    #         return
    #     if is_infront_of_ball:
    #         self.set_intent(goto(self.friend_goal.location  + 5000))
    #         return
    #     #if we're infront of the ball, retreat
    #     self.set_intent(short_shot(self.foe_goal.location))