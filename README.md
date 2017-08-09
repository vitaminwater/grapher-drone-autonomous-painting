# Grapher drone autonomous painting firmware

based on dronekit

## initial setup

disable kernel serial output, by removing the `console=` with serial stuff (keep the one with `console=tty1` in /boo/cmdline.txt, should be something like:

`dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=66b347f9-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait`

set pixhawk baudrate to 921600 by setting `SERIAL2_BAUD` to 921

then configure raspi baudrate, by placing at end of /boot/config.txt:

```
enable_uart=1
init_uart_baud=921600
init_uart_clock=16000000
dtparam=uart0_clkrate=16000000
```
