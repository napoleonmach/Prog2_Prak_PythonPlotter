#"2*math.sin(x)+1" -6 8 40 4
import math
import argparse

def plot_function(expression, x_min, x_max, width, height):
    step = (x_max - x_min) / width
    x_values = [x_min + i * step for i in range(width)]
    y_values = [eval(expression) for x in x_values]

    y_max = max(y_values)
    y_min = min(y_values)

    normalized_y_values = [(y - y_min) / (y_max - y_min) for y in y_values]

    for row in range(height, -1, -1):
        line = ""
        for value in normalized_y_values:
            if row*(1/height)>value and (row-1)*(1/height)<value:
                line+= "*"
            else:
                if True: #TODO: Bedingung der Nulllinie einfügen
                    line+= " "    
                else:
                    line+= "_"
        print(line)





def main():
    parser = argparse.ArgumentParser(description="Matheplotter aus Hogwards")
    parser.add_argument("expression", type=str, help="Funktionsgleichung, z.B., '2*math.sin(x)+1'")
    parser.add_argument("x_min", type=float, help="Minwerte")
    parser.add_argument("x_max", type=float, help="Maxwerte")
    parser.add_argument("width", type=int, help="Darstellungsbreite")
    parser.add_argument("height", type=int, help="Darstellungshoehe")
    args = parser.parse_args()

    plot_function(args.expression, args.x_min, args.x_max, args.width, args.height)

if __name__ == "__main__":
    main()
