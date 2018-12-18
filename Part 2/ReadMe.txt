In this part, our software has 3 main functions, each implements a different function with the following structure:
    —-— main_4_winpoint.py
    |—————- match_samples.py
    |------ get_winpoint.py
    |------ get_telemetry_ur.py
    |------ draw_pic.py

    --- main_4_winpoint.py
    |------ match_samples.py
    |------ get_winpoint.py
    |------ get_telemetry_url.py
    |------ draw_pic.py

    --- main_4_winpoint.py
    |------ match_samples.py
    |------ get_winpoint.py
    |------ get_telemetry_url.py
    |------ draw_pic.py

By running 3 main functions, user can get corresponding results.
Note that get match id (in match_samples.py) have 3 different modes, see comments to decide which mode to use, by default all 3 main functions use random matches sampled up to 14 days earlier.