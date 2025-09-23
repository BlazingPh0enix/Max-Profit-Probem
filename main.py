money_from_theatres = 1500
money_from_pubs = 1000
money_from_commercial_parks = 3000

time_to_build_theatre = 5
time_to_build_pub = 4
time_to_build_commercial_park = 10

def max_profit(total_time):
    if total_time <= 0:
        return [], 0

    # earnings[t] stores max profit using exactly t time
    earnings = [0] * (total_time + 1)
    # choice[t] stores possible buildings chosen at time t
    choice = [[] for _ in range(total_time + 1)]
    
    for t in range(1, total_time + 1):
        # Default: no building (profit from t-1)
        earnings[t] = earnings[t-1]
        choice[t] = choice[t-1][:]
        remaining_time = total_time - t

        if remaining_time > 0:  # Only consider building if there's remaining time        
            # Check for pub
            if t >= time_to_build_pub:
                profit_with_pub = earnings[t - time_to_build_pub] + remaining_time * money_from_pubs
                if profit_with_pub > earnings[t]:
                    earnings[t] = profit_with_pub
                    choice[t] = choice[t - time_to_build_pub] + ['P']
                elif profit_with_pub == earnings[t]:
                    choice[t].append(choice[t - time_to_build_pub] + ['P'])

            # Check for theatre
            if t >= time_to_build_theatre:
                profit_with_theatre = earnings[t - time_to_build_theatre] + remaining_time * money_from_theatres
                if profit_with_theatre > earnings[t]:
                    earnings[t] = profit_with_theatre
                    choice[t] = choice[t - time_to_build_theatre] + ['T']
                elif profit_with_theatre == earnings[t]:
                    choice[t].append(choice[t - time_to_build_theatre] + ['T'])

            # Check for commercial park
            if t >= time_to_build_commercial_park:
                profit_with_park = earnings[t - time_to_build_commercial_park] + remaining_time * money_from_commercial_parks
                if profit_with_park > earnings[t]:
                    earnings[t] = profit_with_park
                    choice[t] = choice[t - time_to_build_commercial_park] + ['C']
                elif profit_with_park == earnings[t]:
                    choice[t].append(choice[t - time_to_build_commercial_park] + ['C'])
    
    # Function to count buildings in a choice list
    def count_buildings(choices):
        T = choices.count('T')
        P = choices.count('P')
        C = choices.count('C')
        return T, P, C
    
    # Collect all combinations that achieve max profit
    max_profit_value = earnings[total_time]
    combinations = []
    for ch in choice[total_time]:
        if isinstance(ch, list):
            combinations.append(count_buildings(ch))
        else:
            combinations.append(count_buildings(choice[total_time]))
    
    # Remove duplicates
    combinations = list(set(combinations))
    
    return combinations, max_profit_value

if __name__ == "__main__":
    n = int(input("Enter the total time available: "))
    combinations, max_profit_value = max_profit(n)
    print("Maximum profit:", max_profit_value)
    print("Solutions:")
    for combo in combinations:
        print(f"T: {combo[0]}, P: {combo[1]}, C: {combo[2]}")