
from stephier import documentmodel as dom
import argparse


def main(step_file: str):
    document = dom.get_document_object(step_file)
    for key, value in document.getEntitiesByNameDict().items():
        print(value[0].name)
    cp = document.getEntityById(569)
    print("HereEndthTheLesson")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", "--stepfile", help="Please enter a step file as argument")
    args = parser.parse_args()
    main(args.stepfile)
