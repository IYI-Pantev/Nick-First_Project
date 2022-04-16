film_budget = float(input())
# дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни
# определен брой статисти, облекло за всеки един статист и декор

# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

walking_actors = int(input())
actor_clothing_price = float(input())
decor = film_budget * 0.10

if walking_actors > 150 :
    actor_clothing_price = actor_clothing_price * 0.90

final_sum = walking_actors * actor_clothing_price + decor
answer = abs(film_budget - final_sum)

if final_sum > film_budget :
    print("Not enough money!")
    print(f"Wingard needs {answer:.2f} leva more.")
elif final_sum <= film_budget :
    print("Action!")
    print(f"Wingard starts filming with {answer:.2f} leva left.")

