import datetime


def next_vdsml_hh() -> str:
    today = datetime.date.today()
    next_thursday = today + datetime.timedelta(((3 - today.weekday()) % 7))
    while True:
        if 15 <= next_thursday.day <= 21:
            next_third_thursday = next_thursday
            break
        else:
            next_date = next_thursday + datetime.timedelta(days=1)
            next_thursday = next_date + datetime.timedelta(
                ((3 - next_date.weekday()) % 7)
            )

    print(f"The next VDSML Happy Hour is {next_third_thursday}")


if __name__ == "__main__":
    next_vdsml_hh()
