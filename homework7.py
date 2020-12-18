text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum consequat iaculis mi vitae facilisis. Fusce porttitor auctor ipsum sit amet consectetur. Vivamus accumsan lorem et ex maximus feugiat. Praesent at molestie ex. Proin auctor facilisis dolor, mattis suscipit libero consequat a. Suspendisse non sapien id ex gravida feugiat sed sed sem. Integer mollis interdum mi a rutrum. Integer sagittis egestas orci ut vulputate. Vivamus vehicula nisi in tortor molestie, id dignissim ligula varius. Ut dictum eros ut posuere pulvinar.

Pellentesque nec imperdiet est. Donec lacinia scelerisque elit, sit amet consequat risus aliquet aliquam. Cras in sodales diam. Duis sed tortor at ex molestie egestas. Fusce dignissim neque ac pharetra tristique. Donec facilisis in leo et vulputate. Cras ut tristique ante, in rhoncus est. Maecenas vitae ligula tempor, elementum tortor convallis, maximus ante. Vivamus rutrum elit magna, id maximus turpis vulputate eget.

Suspendisse sagittis neque massa, ac volutpat mi suscipit non. Cras ut aliquet ligula. Praesent accumsan eget metus et aliquet. Quisque vehicula, magna id egestas pretium, nibh ligula iaculis augue, id hendrerit nulla nisi ac lectus. Nulla porta id lectus sit amet vulputate. Suspendisse finibus efficitur velit vel sodales. Integer augue enim, egestas a cursus ac, tincidunt id purus. Duis facilisis facilisis lorem eget luctus. Nunc feugiat aliquet nunc, nec gravida elit finibus sed. Vestibulum sagittis placerat dolor, a rutrum risus vulputate at. Nullam sit amet fermentum diam.

Sed eleifend luctus neque sed semper. Maecenas non posuere urna. Fusce nunc magna, consectetur nec porta ac, lacinia eget diam. Phasellus ac pulvinar libero. Suspendisse eu tortor sodales, ultricies nulla a, fringilla libero. Etiam rhoncus laoreet erat. Sed interdum massa enim, ut faucibus ipsum maximus et. Sed blandit lorem in consequat luctus. Nulla facilisi. Proin lacus sapien, vehicula non pharetra eget, feugiat id erat. Praesent efficitur ante sit amet ligula mollis, nec volutpat tellus venenatis.

Donec mattis risus sed risus fermentum iaculis. Suspendisse bibendum dapibus elit. Nunc lorem lectus, consectetur et diam eu, suscipit ultricies purus. Etiam semper magna sit amet ligula semper molestie. Suspendisse egestas ligula sit amet mollis luctus. Etiam efficitur, eros vitae interdum dig11nissim, nibh arcu malesuada lectus, et aliquam sapien augue at erat. Nunc maximus nunc at euismod viverra. Donec lorem magna, porttitor eget elit lobortis, viverra tincidunt orci. Suspendisse elementum felis vel luctus semper. Sed maximus pulvinar nibh, ac congue neque dictum sed. Fusce vestibulum est nec mauris pretium, facilisis bibendum lectus commodo. Sed convallis arcu erat, nec consectetur arcu malesuada mattis.
"""

list = text.splitlines()

file = open("text.txt", "w")

for line in list:
	file.write(line + "\n")

file.close()

file = open("text.txt")
print(file.read())
