# ===============================================================================
# Copyright 2018 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
import time

from camera import ToupCamCamera


def main():

    cam = ToupCamCamera()
    cam.open()

    # wait for camera to startup
    time.sleep(2)

    # capture n images
    n = 10
    # every t seconds
    t = 2

    for i in xrange(n):
        path = 'test_image-{:02d}.jpg'.format(i)
        cam.save(path)
        time.sleep(t)


if __name__ == '__main__':
    main()
# ============= EOF =============================================
