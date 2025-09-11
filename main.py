money_from_theatres = 1500
money_from_pubs = 1000
money_from_commercial_parks = 3000

time_to_build_theatre = 5
time_to_build_pub = 4
time_to_build_commercial_park = 10

def max_profit(total_time):

   if total_time <= 0:
      return 0, 0, 0, 0
      
   pub_earnings, theatre_earnings, commercial_park_earnings = [0] * (total_time), [0] * (total_time), [0] * (total_time)

   best_choice = [''] * (total_time)

   for t in range(1, total_time):
      pub_earnings[t] = pub_earnings[t-1]
      theatre_earnings[t] = theatre_earnings[t-1]
      commercial_park_earnings[t] = commercial_park_earnings[t-1]

      if t >= time_to_build_pub:
         earnings = money_from_pubs + pub_earnings[t - time_to_build_pub]
         if earnings > pub_earnings[t]:
            pub_earnings[t] = earnings
            best_choice[t] = 'P'

      if t >= time_to_build_theatre:
         earnings = money_from_theatres + theatre_earnings[t - time_to_build_theatre]
         if earnings > theatre_earnings[t]:
            theatre_earnings[t] = earnings
            best_choice[t] = 'T'

      if t >= time_to_build_commercial_park:
         earnings = money_from_commercial_parks + commercial_park_earnings[t - time_to_build_commercial_park]
         if earnings > commercial_park_earnings[t]:
            commercial_park_earnings[t] = earnings
            best_choice[t] = 'C'

   T, P, C = 0, 0, 0

   i = total_time-1
   while i > 0:
      if best_choice[i] == 'P':
         P += 1
         i -= time_to_build_pub
      elif best_choice[i] == 'T':
         T += 1
         i -= time_to_build_theatre
      elif best_choice[i] == 'C':
         C += 1
         i -= time_to_build_commercial_park
      else:
         i -= 1
   return T, P, C, max(sum(theatre_earnings), sum(pub_earnings), sum(commercial_park_earnings))

if __name__ == "__main__":
    n = int(input("Enter the total time available: "))
    T, P, C, max_profit_value = max_profit(n)
    print("Maximum profit:", max_profit_value)
    print(f"T: {T}, P: {P}, C: {C}")