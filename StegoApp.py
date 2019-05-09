from app_utils.Carrier import *
from app_utils.BitMsg import *
from modules.inject import *
from modules.extract import *


def inject_op():
    print("What's the image path?")
    carrier_path = input()
    carrier = Carrier(carrier_path)
    print("\nPlease type your message")
    msg = BitMsg(input())
    inject(carrier, msg)
    carrier.create_image()
    print("\nImages saved at ./images")


def extract_op():
    print("What's the image path?")
    carrier_path = input()
    carrier = Carrier(carrier_path)
    print("\nWhat's the length of the injected message (in characters)?")
    length = int(input()) * 8
    extract_msg(carrier, length)
    print("\nHidden message:\n", extract_msg(carrier, length), '\n')


if __name__ == "__main__":
    print("Please select:\n\t1. inject\n\t2. extract")
    action = input()
    if action == '1':
        inject_op()
    if action == '2':
        extract_op()

# message example

# image = Carrier(carrier_path)
# msg = BitMsg("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam magna mi, finibus nec hendrerit ac,"
#              "accumsan sed purus. Maecenas porta turpis quis urna feugiat, vitae vulputate lorem ornare. Cras ut mi"
#              "sit amet orci posuere consectetur sit amet eu velit. Aenean tempor luctus sodales. Morbi aliquet diam"
#              "vitae metus pharetra laoreet. Aliquam aliquam urna vitae tempus ultricies. Suspendisse viverra tellus"
#              "sed ante congue iaculis. Sed quis diam leo. Nulla vel tortor id diam ultricies tempus. Proin eget venenatis"
#              "magna. Integer auctor tortor ut quam sagittis pulvinar. Nulla facilisi. Donec ac nibh id leo tristique tempus."
#              "Aliquam hendrerit orci id ante laoreet tempor. Nullam efficitur sit amet urna eleifend commodo. Etiam ex diam,"
#              "eleifend vel ornare sit amet, ultricies quis felis. Nam ultricies elementum vestibulum. Vivamus sem sem, ornare"
#              "ut velit ut, consectetur dictum libero. Aenean venenatis, sapien non feugiat ullamcorper, eros diam iaculis magna,"
#              "sit amet ullamcorper nisi risus sit amet nisl. Nam laoreet libero sed tellus vestibulum, sed mollis velit"
#              "fringilla. Aliquam facilisis vehicula libero id pharetra. Phasellus eget molestie sem. Cras dignissim risus"
#              "malesuada, ultrices ex sed, eleifend nisl. Maecenas in faucibus ipsum. Praesent dolor nulla, faucibus ac semper"
#              "efficitur, fermentum non lectus. Fusce pharetra egestas pretium. Phasellus quis nisi sed diam feugiat dignissim"
#              "quis a risus. Nam sit amet hendrerit dolor. Sed justo sapien, rhoncus at ligula tempus, interdum maximus magna."
#              "Aliquam sit amet turpis non libero commodo ultrices at nec mi. Nam id vestibulum diam, a dapibus turpis."
#              "Curabitur ullamcorper ipsum et enim facilisis, et vulputate mauris pharetra. Suspendisse sagittis mollis"
#              "facilisis. Integer luctus posuere tincidunt. Sed posuere, sapien vel tristique egestas, ligula arcu sodales"
#              "urna, in tempus nisi augue lobortis eros. Quisque consequat non velit et placerat. Mauris ut tincidunt dolor,"
#              "rutrum tincidunt ligula. Sed non dui ac eros vestibulum semper. Sed vel dapibus risus, id euismod nisi."
#              "In tellus felis, pellentesque vitae ex eget, tempor semper orci. Donec in ex odio. Curabitur aliquam dapibus"
#              "mi quis varius. Aliquam finibus neque eget elit pellentesque ornare. Etiam auctor, neque id iaculis maximus,"
#              "tortor neque cursus nulla, sit amet dictum neque lorem ac nisl. Morbi sit amet iaculis dolor. Phasellus"
#              "nec tempus eros, vel porta erat.")
