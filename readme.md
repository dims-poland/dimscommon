# Common scripts for dims project

## Installation

To install localy:

```bash
pip install ./dimscommon
```

than to use `Trigger`

```python
import dimscommon.trigger as tg
```

or to use `DataCollection`:

```python
import dimscommon.datacollection as dc
```

Testing db can be launched using `docker-compose`

```python
docker-compose up
```


## dimscommon.trigger

### Used structures

```python
"""
Object representing a 2 dimentional vector
"""
Vec2 = namedtuple('Vec2', ['x', 'y'])
```
```python
"""
Object repersenting Rectangle
"""
Rect = namedtuple('Rect', ['min_x', 'min_y', 'max_x', 'max_y'])
```
```python
"""
Names used to extract information from csv to Trigger object
"""
field_names = [
    'file',  # Path: file
    'start_frame',  # int: First frame on which event was recorded
    'end_frame',  # int: Last frame on which event was recorded
    'bounding_rect',  # @Rect: bounding rectangle
    'additional_data'  # dictionary of algorithm specific information about the trigger
]
"""
Common interface object for a trigger
"""
Trigger = namedtuple('Trigger', field_names)
```


### Creating Trigger object
```python
""" Simple create trigger (only for future possible extension) """
def create_trigger(file, start_frame, end_frame, rect, additional_data)
```

```python
""" Create trigger without need to manualy create Rect object """
def create_trigger_flat(file, start_frame, end_frame, box_min_x, box_min_y,
                        box_max_x, box_max_y, additional_data)
```

```python
""" Creates trigger from dictionary field names need to be the same as @field_names """
def create_trigger_dict(dictionary)
```

### Convinience methods

```python
"""
Get the arr of frames and combine them into one
(by getting max pixel value)
"""
def combine_frames(frame_list: np.array):

""" Cuts out the rect from given frame """
def cut_rect_from_frame(frame: np.array, r: Rect) -> np.array:

""" Calculate center of a @Trigger """
def get_center(trigger: Trigger) -> Vec2:

""" Calculate number of a section containing center of the @Trigger """
def get_section(trigger: Trigger) -> int:

""" Cutout section Rect """
def section_rect(trigger: Trigger) -> Rect:

""" Creates Rect with some offeset from the center """
def center_rect(trigger: Trigger, size: Vec2, crop_method="move") -> Rect:

""" Get frames from Trigger """
def get_frames(trigger: Trigger) -> np.array:

"""
Given an array of frames creates and animation
TODO: make it faster with:
https://github.com/vrabelmichal/dims_experimentation/blob/207f37ef4d41dbae366570a9a58ae58ce724f3af/visualization.py#L95-L142
"""
def animate(frame_list: np.array, interactive=True, file="out.mp4", size=None):


""" Draw a rectangle on a bigger image """
def mark_rect(frame: np.array, rect: Rect, color=(0, 255, 0), thickness=2):

def get_id(trigger: Trigger):

""" Connect to db and get events with ids on @trigger_ids """
def get_triggers_from_db(trigger_ids: List[int]):
```

# Comunicating with labeling server

To upload triggers to the labeling server first you need to create datacollection
on the server by calling:

```python
def create_datacollection(url, collection_name: str,
                          collection_parameter_names: List[str],
                          parameter_values: List[str],
                          additional_trigger_info: List[str]) -> int
```

You will get a collection ID which can be later used to push triggers to the 
labeling server using:

```python
def upload_trigger(trigger: Trigger, collection_id: int, url: str) -> int
```

This function will add the trigger to the labbeling studio and the DB and return 
the global trigger id that assigned to it by the server for later use.
