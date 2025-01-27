# Development Tasks & Notes

- [x] Initial measurements and CAD modeling of Lubitel 166B back
  
- [x] Reverse engineering the Instax Mini film cartridge and film release mechanism

- [x] Design preliminary film back attachment mechanism

- [ ] Test film release mechanism with real cartridge and find appropriate stepper motor settings. Initially with A4988 drivers and micropython.

- [ ] Design complete film back, including light seals

- [ ] Rust RP2040 code for stepper motor control. At this point, it should be able to take photos and develop film. Use TMC drivers, as well as integrate sensorless homing for the pushing mechanism

- [ ] Figure out how to adjust focus to the film plane (there is about a 0.5mm difference between the old film back plane and the new one)

- [ ] Nice UI on OLED or Eink display

- [ ] Auto metering system with a light sensor

- [ ] Film counter with persistent memory

- [ ] Flash and calibratiion with metering

- [ ] Battery power system

- [ ] Finalize design and make a PCB
