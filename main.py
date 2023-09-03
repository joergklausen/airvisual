#%%
import os
from airvisual.airvisual import get_recent_data, plot_data

x15a = "https://device.iqair.com/v2/64b79227b6f7b1125b019970"
wich = "https://device.iqair.com/v2/64b78e3ed49ffdbbf25ce862"
twrg = "https://device.iqair.com/v2/64ad7a78e939e8f45b826839"

path = os.path.join(os.path.curdir, "figures")
df_x15a = get_recent_data(x15a)
plot_data(df_x15a, title="X15A", linestyle=":", path=path)

df_wich = get_recent_data(wich)
plot_data(df_wich, title="WICH", linestyle="-.", path=path)

df_twrg = get_recent_data(twrg)
plot_data(df_twrg, title="TWRG", linestyle="-", path=path)
