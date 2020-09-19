import random

def number_guessing_game():
    my_number = random.randint(1, 100)

    print("\n１から１００までの番号を考えてます。")
    print("番号を当ててみよう！")
    
    while True:
        player_number = int(input())

        if player_number == my_number:
            print("\nすごい！当たった！")
            play_again = input("また遊ぶ？ (y/n): ")
            if play_again == 'n':
                print("じゃあね〜")
                raise SystemExit
            else:
                number_guessing_game()
        elif player_number >= my_number:
            print("\n高すぎ！")
        elif player_number <= my_number:
            print("\n低すぎ！")

number_guessing_game()