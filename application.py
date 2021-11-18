import constants
import random


def Clean_up_data():
    player_set, experienced_name_list, inexperienced_name_list = [], [], []
    for people in constants.PLAYERS:
        player_dic = {}
        for key, value in people.items():            
            if key == 'name':
                player_dic[key] = value
            elif key == 'guardians':                
                player_dic[key] = value.split(' and ')
            elif key == 'experience':
                if value == 'YES':
                    player_dic[key] = True
                    experienced_name_list.append(player_dic['name'])
                elif value == 'NO':
                    player_dic[key] = False
                    inexperienced_name_list.append(player_dic['name'])
                else:
                    print('Can\'t defined experience bool.')
            elif key == 'height':
                try:
                    height_num,_ = value.split()
                    player_dic[key] = int(height_num)
                except:
                    print('Can\'t defined height int.')
        player_set.append(player_dic)    
    return player_set, experienced_name_list, inexperienced_name_list


def welcome():    
    while True:
        try:
            # Show the menu with the user's options
            print('\nBASKETBALL TEAM STATS TOOL\n')
            print('---- MENU ----\n')
            print('Here are your choices:\n')
            print('1) Display Team Stats\n')
            print('2) Quit\n')
            user_option = int(input('Enter an option: '))
            print('\n')
        except:
            print('That is not a valid value. Please try again.')
        else:
            if user_option == 2:
                print('Good bye.')
                break
            elif user_option == 1:
                try:
                    # Team & Total players       
                    print('Here are your choices:\n')

                    for index, team in enumerate(constants.TEAMS, start=1):
                        print(f'{index}) {team}')                    
                    
                    user_team = int(input('\nEnter an option: '))
                    num_players_team = int(len(constants.PLAYERS) / len(constants.TEAMS))
                    
                    print(f'Team: {constants.TEAMS[user_team - 1]} Stats')
                    print('-------------------')
                    print(f'Total players: {num_players_team}\n')
                    
                    # Players on team & Total number of experienced players & Total number of inexperienced players    
                    team_experienced_name_list = random.sample(experienced_name_list, len(experienced_name_list) // int(len(constants.TEAMS)))
                    team_inexperienced_name_list = random.sample(inexperienced_name_list, len(inexperienced_name_list) // int(len(constants.TEAMS)))
                    team_player_name_list = team_experienced_name_list + team_inexperienced_name_list
                                                         
                    print(f'Players on team:')
                    print(', '.join(team_player_name_list) + '.')
                    print(f'\nTotal number of experienced players: {len(team_experienced_name_list)}\n')
                    print(f'Total number of inexperienced players: {len(team_inexperienced_name_list)}\n')
                    
                    # Average height of the team & The guardian names of all the players on the team
                    team_player_height,  guardian_name_list = 0, []

                    for now in player_set:
                        if now['name'] in team_player_name_list:
                            team_player_height += now['height']
                            guardian_name_list += now['guardians']

                    team_player_height = round(team_player_height / num_players_team, 2)                    
                    
                    print(f'Average height of the team: {team_player_height}\n')
                    print('The guardian names of all the players on the team:')
                    print(', '.join(guardian_name_list) + '.')

                    # Press ENTER to continue
                    input("\nPress ENTER to continue...\n")                   

                except:
                    print('That is not a valid value. Please try again.')
            else:
                print('That is not a valid value. Please try again.')
        '''
        finally:
            print('fiiiiiiiiiiiiiiii')#if break, still run
        print('ooooooooooooout')#if break, still not run
        '''



if __name__ == '__main__':
    # Clean up data
    player_set, experienced_name_list, inexperienced_name_list = Clean_up_data()

    # Show the menu & Team balancing & Display Stats    
    welcome()
    
    






