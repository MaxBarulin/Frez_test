import math


# Удельное сопротивление резанию для различных материалов
kc_values = {
    "Углеродистая сталь": 1800,
    "Низколегированная сталь": 2200,
    "Высоколегированная сталь": 2500,
    "Чугун": 1500,
    "Нержавеющая сталь": 2800,
    "Алюминиевые сплавы": 700,
    "Латунь": 1000,
    "Медные сплавы": 1200,
    "Титан и его сплавы": 3000,
    "Никелевые сплавы": 3500,
    "Пластики": 500
}

# Основная функция
def main():
    while True:
        # Шаг 0: Ввод мощности шпинделя
        spindle_power_input = input("\nВведите доступную мощность шпинделя (кВт) или оставьте пустым для пропуска: ")
        spindle_power = float(spindle_power_input) if spindle_power_input else None

        # Шаг 3: Выбор материала обработки
        print("\nВыберите материал обработки из списка:")
        materials = list(kc_values.keys())
        for i, material in enumerate(materials, start=1):
            print(f"{i}. {material}")

        material_choice = int(input("Введите номер выбранного материала: ")) - 1
        material = materials[material_choice]
        # print(material) # проверяем выбор материала обработки
        kc = kc_values.get(material)
        # print(kc) # проверяем значение cорп. для выбранного мат.

        D = float(input("\nВведите диаметр фрезы (мм): "))

        z = int(input("Введите количество зубьев фрезы: "))

        t = float(input("Введите глубину прохода (мм): "))

        L = float(input("Введите длину обработки L (мм): "))

        S = float(input("Введите подачу S (мм/мин): "))

        n = float(input("Введите частоту вращения шпинделя n (об/мин): "))
        print("")
        # расчет скорости резания
        V = (math.pi * D * n)/1000

        # расчет подачи
        F = S/n

        # расчет
        Fz = F/z

        # расчет необходимой мощности станка
        P = round((kc * V * t * F)/(60 * 1000), 1)

        print("Заданные режимы резания")
        print(f"Диаметр фрезы (мм): {D}")
        print(f"Количество зубьев фрезы: {z}")
        print(f"глубину прохода (мм): {t}")
        print(f"длину обработки (мм): {L}")
        print(f"Подача (мм/мин): {S:.2f}")
        print(f"Скорость резания (м/мин): {V:.2f}")
        print(f"Частота вращения шпинделя (об./мин): {n:.2f}")
        print(f"Подача на оборот (мм/об.): {F:.2f}")
        print(f"Подача на зуб за оборот (мм/зуб): {Fz:.2f}")
        print(f"Требуемая мощность резания (кВт): {P:.2f}")
        print(f"Время обработки (мин): {L / S:.2f}")

        if spindle_power is None:
            print("\nРасчет без подгонки мощности шпинделя")

        elif spindle_power < P:
            print(f"\nВНИМАНИЕ: Требуемая мощность резания ({P:.2f} кВт)"
                  f"\nпревышает доступную мощность шпинделя ({spindle_power} кВт).\n")

            i = True
            ii = True
            S_opt = 0
            P_opt = 0

            while i:
                S_opt = S - 5
                F_opt = S_opt / n
                # Fz_opt = F_opt / z
                P_opt = round((kc * V * t * F_opt) / (60 * 1000), 1)
                S = S_opt

                if P_opt <= spindle_power:
                    i = False

            while ii:
                n -= 5
                n_opt = n
                F_optt = S_opt / n_opt
                Fz_optt = F_optt / z

                if F_optt >= F:
                    ii = False

            V_opt = (math.pi * D * n_opt) / 1000

            print("Рекомендуемые режимы резания")
            print(f"Диаметр фрезы (мм): {D}")
            print(f"Количество зубьев фрезы: {z}")
            print(f"глубину прохода (мм): {t}")
            print(f"длину обработки (мм): {L}")
            print(f"Подача (мм/мин): {S_opt:.2f}")
            print(f"Скорость резания (м/мин): {V_opt:.2f}")
            print(f"Частота вращения шпинделя (об./мин): {n_opt:.2f}")
            print(f"Подача на оборот (мм/об.): {F_optt:.2f}")
            print(f"Подача на зуб за оборот (мм/зуб): {Fz_optt:.2f}")
            print(f"Требуемая мощность резания (кВт): {P_opt:.2f}")
            print(f"Время обработки (мин): {L / S_opt:.2f}")


main()

# def coo(x):
        #     num = x
        #
        #     def mem():
        #         nonlocal num
        #         num += 1
        #         return num
        #
        #     return mem
        #
        # t = coo(5)
        # print(t())  # Вывод: 1
        # print(t())  # Вывод: 2