from util.fx_util import read_file


class ConvertRate:

    db_path = "db/fx_rate.json"

    def convert_rate(self):
        currency = read_file(self.db_path)

        source = input("Source Currency: ").upper()
        target = input("Target Currency: ").upper()
        amount = float(input("Amount: "))

        try:
            fx_rate = next(
                fx_rate for fx_rate in currency
                if fx_rate["source"] == source and fx_rate["target"] == target
            )

            rate = float(fx_rate["rate"])
            converted_amount = amount * rate

            print(f"Converted Amt: {converted_amount}")

        except:
            print(f"Your Input {source} and {target} is NOT FOUND!")
