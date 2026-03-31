# tr0bot ROS 2 Workspace (Desktop Side)

Этот репозиторий содержит полный воркспейс `dev_ws` для проекта мобильного робота `tr0bot`. 

> [!IMPORTANT]
> Данная часть проекта предназначена для **настольного компьютера** (управляющей станции). Код для бортового компьютера робота будет добавлен позже.

## Структура проекта
- `src/tr0bot` — основной пакет с описанием робота (URDF), параметрами навигации и запусками.
- `src/serial_motor_demo` — драйверы для моторов.
- `src/rosbridge_suite` — мост для связи с веб-интерфейсами.
- `section_8_research.md` — документация по исследованию эффективности навигации.

## Установка
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/tetram1t/tr0bot.git
   ```
2. Установите зависимости:
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
   ```
3. Соберите проект:
   ```bash
   colcon build
   ```

## Запуск симуляции
```bash
ros2 launch tr0bot launch_sim.launch.py
```
