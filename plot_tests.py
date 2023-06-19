import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_tests(root,test_results, num_tests, num_services):

    plot_win = Toplevel(root)
    root.iconbitmap("icon.ico")
    plot_win.geometry("1740x580+120+350")
    plot_win.title("Internet Speed Checker - Analyzing data")
    plot_win.grab_set()

    df = pd.DataFrame(test_results)
    df.rename(columns={'service_name': 'test cycle', 'ping': 'ping, ms', 'upload_speed': 'upload, Mb/s',
                                    'download_speed': 'download, Mb/s', 'duration': 'duration, s', 'test_date': 'date',
                                    'test_time': 'time'}, inplace=True)

    # ping_tests_draw
    df_ping = df[['test cycle', 'ping, ms']]
    df_ping.set_index('test cycle', inplace=True)

    figure1 = plt.Figure(figsize=(6, 5), dpi=90)
    ax1 = figure1.add_subplot(3, 1, (1, 2), facecolor="lightgrey")
    bar1 = FigureCanvasTkAgg(figure1, plot_win)
    bar1.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)
    df_ping.plot(kind='bar', legend=True, ax=ax1, color='brown')
    ax1.set_title(f'Ping data ({num_tests} tests, {num_services} services)')

    ping_info = Label(plot_win, text=f"Average ping: {round(df_ping['ping, ms'].mean(), 1)} ms", fg="red")
    ping_info.config(font=('Courier bold', 14))
    ping_info.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
    ping_minmax = Label(plot_win, text=f"min. {df_ping['ping, ms'].min()} ms,  max. {df_ping['ping, ms'].max()} ms")
    ping_minmax.grid(row=2, column=0, padx=5)

    #upload_tests_draw
    df_upload = df[['test cycle', 'upload, Mb/s']]
    df_upload.set_index('test cycle', inplace=True)

    figure2 = plt.Figure(figsize=(6, 5), dpi=90)
    ax2 = figure2.add_subplot(3, 1, (1, 2), facecolor="lightgrey")
    bar2 = FigureCanvasTkAgg(figure2, plot_win)
    bar2.get_tk_widget().grid(row=0, column=1, padx=20, pady=20)
    df_upload.plot(kind='bar', legend=True, ax=ax2, color='green')
    ax2.set_title(f'Upload speed data ({num_tests} tests, {num_services} services)')

    upload_info = Label(plot_win, text=f"Average upload speed: {round(df_upload['upload, Mb/s'].mean(), 1)} Mb/s",
                        fg="green")
    upload_info.config(font=('Courier bold', 14))
    upload_info.grid(row=1, column=1, columnspan=1, padx=5, pady=5)
    upload_minmax = Label(plot_win,
                          text=f"min. {df_upload['upload, Mb/s'].min()} Mb/s,  max. {df_upload['upload, Mb/s'].max()} Mb/s")
    upload_minmax.grid(row=2, column=1, padx=5)

    #download_tests_draw
    df_download = df[['test cycle', 'download, Mb/s']]
    df_download.set_index('test cycle', inplace=True)

    figure3 = plt.Figure(figsize=(6, 5), dpi=90)
    ax3 = figure3.add_subplot(3, 1, (1, 2), facecolor="lightgrey")
    bar3 = FigureCanvasTkAgg(figure3, plot_win)
    bar3.get_tk_widget().grid(row=0, column=2, padx=20, pady=20)
    df_download.plot(kind='bar', legend=True, ax=ax3, color='blue')
    ax3.set_title(f'Download speed data ({num_tests} tests, {num_services} services)')

    download_info = Label(plot_win,
                          text=f"Average download speed: {round(df_download['download, Mb/s'].mean(), 1)} Mb/s",
                          fg="blue")
    download_info.config(font=('Courier bold', 14))
    download_info.grid(row=1, column=2, columnspan=1, padx=5, pady=5)
    download_minmax = Label(plot_win,
                            text=f"min. {df_download['download, Mb/s'].min()} Mb/s,  max. {df_download['download, Mb/s'].max()} Mb/s")
    download_minmax.grid(row=2, column=2, padx=5)
