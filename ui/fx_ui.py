from bll.addORupdate_fx_rate import AddOrUpdateFXRate
from bll.converted_rate import ConvertRate
from dal.display_rates import DisplayRates


class Menu:

    def main(self):
        add_fx = AddOrUpdateFXRate()
        convert = ConvertRate()
        display = DisplayRates()

        commands = {
            "1": add_fx.add_fx_rate,
            "2": display.display_rates,
            "3": convert.convert_rate,
            "X": exit
        }

        print("========FX_APP========")
        choices = input(
            "1: Add FX Rate\n"
            "2: List FX Rate\n"
            "3: Convert Rate\n"
            "X: Exit\n"
            "Enter your choice: "
        ).upper()

        command = commands.get(choices)

        if command is None:
            print("Invalid choice. Please try again.")
        elif choices == "X":
            return
        else:
            command()

        return self.main()
