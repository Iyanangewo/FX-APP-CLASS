from util.fx_util import read_file, write_file

db_path = "db/fx_rate.json"

class AddOrUpdateFXRate:
    def add_fx_rate(self):
        currency = read_file(db_path)

        source = input("Source Currency: ").upper()
        target = input("Target Currency: ").upper()
        rate = input("Fx Rate: ")

        fx_rate = {
            "source": source,
            "target": target,
            "rate": rate
        }

        for existing_rate in currency:
            if (existing_rate["source"] == source and existing_rate["target"] == target):
                existing_rate["rate"] = rate

                write_file(db_path, currency)

                print("Existing FX rate has been updated")
                return

        currency.append(fx_rate)
        write_file(db_path, currency)

        print("FX rate has been added")
