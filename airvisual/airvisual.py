# %%
import os
import json
import pandas as pd
import polars as pl
import requests
import matplotlib.pyplot as plt

def get_api_key(file: str) -> str:
    with open("api.key", "r") as fh:
        return fh.read()


def get_recent_data(url: str, type="hourly") -> pl.DataFrame:
    try:
        with requests.get(url=url, stream=True) as r:
            df = pd.DataFrame(json.loads(r.text))
            df = pl.DataFrame(df['historical'][type])

            # extract PM concentrations
            df = df.with_columns([
                    pl.col("hm").alias("rh"),
                    pl.col("ts").str.to_datetime().alias("dtm"),
                    pl.col("pm25").struct.field("conc").alias("pm2.5"), 
                    pl.col("pm10").struct.field("conc").alias("pm10"), 
                 ]).select("dtm", "co2", "pm1", "pm2.5", "pm10", "tp", "rh", "pr")

        return df
    
    except Exception as err:
        print(err)

def plot_data(df: pl.DataFrame, title: str="", linestyle: str="-", path: str=None) -> None:
    if df.is_empty() or df is None:
        return
    try:
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True, 
                                    figsize=(12, 18), dpi=180)
        ax1.plot(df['dtm'], df['tp'], label="T (°C)", linestyle=linestyle)
        ax1.plot(df['dtm'], df['rh'], label="RH (%)", linestyle=linestyle)
        ax1.legend()
        ax1.set_title(title)
        ax2.plot(df['dtm'], df['pm1'], label="PM1 (ug/m3)", linestyle=linestyle)
        ax2.plot(df['dtm'], df['pm2.5'], label="PM2.5 (ug/m3)", linestyle=linestyle)
        ax2.plot(df['dtm'], df['pm10'], label="PM10 (ug/m3)", linestyle=linestyle)
        ax2.legend()
        ax3.plot(df['dtm'], df['co2'], label="CO2 (ppm)", linestyle=linestyle)
        ax3.legend()
        fig.autofmt_xdate()
        plt.show()

        if path:
            os.makedirs(path, exist_ok=True) 
            fig.savefig(os.path.join(path, f"{title}.png"))
            fig.savefig(os.path.join(path, f"{title}.pdf"))

    except Exception as err:
        print(err)


def get_data(url: str, sensor_id: str, begin: str, end: str) -> pl.DataFrame:
    try:
        print("TODO")

    except Exception as err:
        print(err)
        return err


if __name__ == "__main__":
    pass


# from requests.exceptions import ChunkedEncodingError as ChunkedEncodingError

# try:
#    with requests.get(url, token, auth, stream=True) as r:
#     with open("output.json", "w") as f:
#        for chunk in r.iter_lines():
#            if chunk:
#                 chunk = chunk.decode("utf-8")
#                 f.write(chunk)
#            else:
#                 logging.info("No data returned.")

# except ChunkedEncodingError as e:
#       logging.info(f"Error detected - {e}")
