
from util.fx_util import read_file


class DisplayRates:

    db_path = "db/fx_rate.json"

    def display_rates(self):
        currency = read_file(self.db_path)

        print(
            "Source CCY".ljust(12),
            "Target CCY".ljust(12),
            "Rate".ljust(12)
        )

        for fx_rate in currency:
            print(
                fx_rate["source"].ljust(12),
                fx_rate["target"].ljust(12),
                str(fx_rate["rate"]).ljust(12)
            )
