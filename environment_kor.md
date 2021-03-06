## Environment Table of Contents

- [Starcraft II](#starcraft-ii)
    - [What is StarCraft II](#what-is-starcraft-ii)
    - [Versions](#versions)
    - [Game and Action Speed](#game-and-action-speed)
        - [Game speed](#game-speed)
        - [APM 계산](#apm-계산)
        - [APM과 공평함](#apm과-공평함)
    - [결정론과 무작위성](#결정론과-무작위성)
- [행동과 관찰](#행동과-관찰)
    - [관찰](#관찰)
        - [공간/시각](#공간/시각)
            - [RGB Pixels](#rgb-pixels)
            - [Feature layers](#feature-layers)
            - [Minimap](#minimap)
            - [Screen](#screen)
        - [Structured](#structured)
            - [일반적인 플레이어 정보](#일반적인-플레이어-정보)
            - [제어 그룹](#제어-그룹)
            - [Single Select](#single-select)
            - [Multi Select](#multi-select)
            - [Cargo](#cargo)
            - [BuildQueue](#build-queue)
            - [AvailableActions](#available-actions)
            - [LastActions](#last-actions)
            - [ActionsResult](#action-result)
            - [Alerts](#alerts)
    - [Actions](#actions)
        - [List of actions](#list-of-actions)
        - [Action categories](#action-categories)
        - [General vs Specific actions](#general-vs-specific-actions)
        - [Example usage](#example-usage)
- [RL Environment](#rl-environment)
    - [Environment wrappers](#environment-wrappers)
- [Agents](#agents)

<!-- /TOC -->

## StarCraft II

### What is StarCraft II

[StarCraft II](https://en.wikipedia.org/wiki/StarCraft_II:_Legacy_of_the_Void)
는 [Blizzard](http://blizzard.com/)가 만든 [Real Time Strategy
(RTS)](https://en.wikipedia.org/wiki/Real-time_strategy) 게임으로 가장 성공적인 RTS게임 중 하나인 [StarCraft
Broodwar](https://en.wikipedia.org/wiki/StarCraft:_Brood_War)의 후계자이다. StarCraft II는 수백만명이 플레이하며 [professional league](https://wcs.starcraft2.com/en-us/)를 가지고 있다.

[스타크래프트의 목표](http://us.battle.net/sc2/en/game/guide/whats-sc2)는 기지를 건설하고, 경제를 관리하고, 군대를 건설하고, 적을 섬멸하는 것이다. 플레이어는 제3자의 시점에서 기지와 군대를 통제한 다음 플레이어의 부대를 최대의 효과를 얻기 위해 멀티태스킹과 섬세한 관리를 한다. 스타크래프트에는 전략과 유닛이 서로 다른 세가지 종족이 있다.  -> :
[테란(Terran)](https://www.youtube.com/watch?v=Fmu8PsUDDtQ),
[프로토스(Protoss)](https://www.youtube.com/watch?v=m0g0MpllFCs),
[저그(Zerg)](https://www.youtube.com/watch?v=Lq74R7wWAnQ)

대부분의 사람들이 [배틀넷(Battle.net)](http://battle.net/sc2/en/)에서 멀티플레이를 하지만 이 게임에는 싱글 플레이어 캠페인이 있다. 기본 내장된 봇(bots)이 있지만 상당히 약하고 예측가능한 플레이를 한다.

온라인에서 스타크래프트에 대해 배우기 위해서는 [배틀넷(Battle.net)](http://battle.net/sc2/en/),
[리퀴드 위키피디아(Liquipedia)](http://liquipedia.net/starcraft2/StarCraft) 그리고
[위키(Wikia)](http://starcraft.wikia.com/)가 있다. 지도 제작은 
[SC2Mapster](https://sc2mapster.gamepedia.com/SC2Mapster_Wiki)를 참고한다.

### Versions

블리자드(게임회사)는 정기적으로 스타크래프트II를 업데이트한다. 이러한 업데이트는 매월 실시되며, 새로운 기능이 도입 되거나, 게임을 보다 균등(밸런스)하게 만들기 위해 사소한 게임 플레이와 밸런스 변경이 있는 경우가 많다. 리플레이(replay)는 특정 버전에 의존된다.(버전에 따라 리플레이 파일이 다르다.)

### Game and Action Speed

실시간 전략 게임은 게임이 실시간으로 진행된다는 것을 의미한다. 하지만 실제 시뮬레이션은 게임 속도[game speed](http://wiki.teamliquid.net/starcraft2/Game_Speed)에 따라 16~22회 업데이트 되며 중간 렌더링 프레임은 모두 보간된다.

#### Game speed

Acting through an API allows you to control the clock. Instead of running at
16-22 steps per second, you can step as fast or as slow as you want, when you
want. This allows you to run much faster than real-time if the agent is capable,
or much slower if the agent needs to pause to spend some time learning. This
also means there is never any lag. The max speed depends on the step_mul/render
frequency, and the scene complexity/unit count. 10x real-time is not uncommon
and can be much higher for simple maps.

#### APM 계산

The game calculates and reports APM in a non-obvious way. It isn't obvious how
to count the action of moving the camera with edge scrolling, or how many
actions is building a building. Here are the rules of how it's actually counted
by the game.

There are actually two types reported by the game:

*   Actions Per Minute (APM): counts every action.
*   Effective Actions Per Minute (EPM): filters out actions that have no effect
    (eg: redundant selections).

Different actions count as different number of actions:

*   Commands with target = 2 (eg: move, attack, build building)
*   Commands with no target = 1 (eg: stop, train unit, unload cargo)
*   Smart = 1 (right click)
*   Selection and control groups = 1
*   Everything else = 0 (eg: camera movement)

The in game replay UI exposes this with two different time intervals: average
(average over the entire game so far), and current (average over the last 5
seconds). The API only exposes the average APM.

#### APM과 공평함

Humans can't do one action per frame. They range from 30-500 actions per minute
(APM), with 30 being a beginner, 60-100 being average, and professionals
being >200 (over 3 per second!). This is trivial compared to what a fast bot is
capable of though. With the [BWAPI](http://bwapi.github.io/) they control units
individually and routinely go over 5000 APM accomplishing things that are
clearly impossible for humans and considered
[unfair](https://youtu.be/IKVFZ28ybQs?t=45s) or even
[broken](https://youtu.be/0EYH-csTttw?t=28s). Even without controlling the units
individually it would be unfair to be able to act much faster with high
precision.

To at least resemble playing fairly it is a good idea to artificially limit the
APM. The easy way is to limit how often the agent gets observations and can make
an action, and limit it to one action per observation. For example you can do
this by only taking every `N`th observation, where `N` is up for debate. A value
of 20 is roughly equal to 50 apm while 5 is roughly 200 apm, so that's a
reasonable range to play with. A more sophisticated way is to give the agent
every observation but limit the number of actions that actually have an effect,
forcing it to mainly make no-ops which wouldn't count as actions.

It's probably better to consider all actions as equivalent, including camera
movement, since allowing very fast camera movement could allow agents to cheat.

### 결정론과 무작위성

Starcraft II is mostly deterministic, but it does have some randomness mainly
for cosmetic reasons. The two main random elements are weapon speed and update
order.

Weapon randomness is essentially how fast a unit can get its next shot off after
firing and is between -1 to +2 game steps for almost all units. The idea
being that a group of marines may all start firing together, but the minor
random +/- for the next shot will make the group look less robotic and prevent
them from firing in sync forever. This also means a fair matchup (eg 1v1 marine)
will result in a random outcome.

The update order is random and determines the order of events in a given game
loop. For example, if you have two High Templar that cast feedback on each other
on the same game loop, it will be random which one performs the damage first and
wins.

Unit auto-targeting is deterministic, but complicated. It is based on weapon
scan distance, threat and assistance. Units will consider any enemies with
weapon a higher threat than those without, and enemies that can return fire will
be a higher priority than those that can’t return fire. Units that can't return
fire (eg a missile turret vs a marine) but that are attacking an allied unit (eg
a medivac) will trigger a call for help and increase the priority. A healer
raises its priority when it is healing. If two targets have the same priority
the nearest one will be chosen.

These sources of randomness can be removed/mitigated by setting a random seed.
Replays work by saving the game setup including the random seed, as well as the
list of actions by all players, and then playing forward the simulation.

## 행동과 관찰

Starcraft II has a very rich action and observation space. The game outputs
both spatial/visual and structured elements. The structured elements are given
because there is a lot of text and numbers which agents aren't expected to learn
to read, especially at low resolution. It's also because it's hard to reverse
replays back to exactly the same visuals that the human saw.

__Important Note:__

Spatial observations are in y-major screen coordinate space as `(y, x)`. Actions
that require points on the screen or the minimap, however, expect the
coordinates as `(x, y)`. The origin `(0, 0)` is at the top-left corner in both
cases.

See the [scripted agents](../pysc2/agents/scripted_agent.py) for an example of
passing a screen coordinate to an action:

```python
    # Spatial observations have the y-coordinate first:
    y, x = (obs.observation["feature_screen"][_PLAYER_RELATIVE] == _PLAYER_NEUTRAL).nonzero()

    # Actions expect x-coordinate first:
    target = [int(x.mean()), int(y.mean())]
    action = actions.FunctionCall.Move_screen("now", target)
```

### 관찰

#### 공간/시각

##### RGB Pixels

RGB pixels are available for both the main screen area as well as for the
minimap at a resolution of your choice. This uses the same perspective camera as
a human would see, but doesn't include all the extra chrome around the screen
like the command card, selection box, build queue, etc. They are exposed as
`rgb_screen` and `rgb_minimap`.

##### Feature layers

The game also exposes feature layers. They represent roughly the same
information as RGB pixels except that the information is decomposed and
structured. There are ~25 feature layers broken down between the screen and
minimap and exposed as `feature_screen` and `feature_minimap`.

The full list is defined in `pysc2.lib.features`.

###### Minimap

The minimap is a low resolution view of the entire map. It gives an overview of
everything going on, but with less detail than the screen.

You can specify the resolution of the minimap. Maps range from
32-256<sup>2</sup>, with common human maps in the 100-256<sup>2</sup> range.
Humans playing at 1080p get a resolution of ~250<sup>2</sup> in the bottom left
corner of their screen.

These are the minimap feature layers:

*   **height_map**: Shows the terrain levels.
*   **visibility**: Which part of the map are hidden, have been seen or are
    currently visible.
*   **creep**: Which parts have zerg creep.
*   **camera**: Which part of the map are visible in the screen layers.
*   **player_id**: Who owns the units, with absolute ids.
*   **player_relative**: Which units are friendly vs hostile. Takes values in
    [0, 4], denoting [background, self, ally, neutral, enemy] units
    respectively.
*   **selected**: Which units are selected.

###### Screen

The screen is a higher resolution view of part of the map.

It is rendered from a top down orthogonal camera, as opposed to a perspective
camera that a human would get in a real game. This makes certain visuals harder
(eg you can't see elevation by size), but it also makes other things easier (eg
units don't change size as they or the camera moves). This also means that the
visible area is a rectangular part of the map, as opposed to the more
trapezoidal shape in the real game. This means there are bits of the map that an
agent can see that humans can't, and vice versa, but it is roughly similar.

A small unit (eg marine or zergling) is ~0.75 game units across. The camera is
24 game units wide. If you specify a screen resolution of 32<sup>2</sup>, that
means a unit will be 1 pixel wide, meaning you have very low accuracy of its
location. If you have a large group of them you may not be able to tell how many
of them you have. A resolution of at least 64<sup>2</sup> is recommended to be
playable.

These are the screen feature layers:

*   **height_map**: Shows the terrain levels.
*   **visibility**: Which part of the map are hidden, have been seen or are
    currently visible.
*   **creep**: Which parts have zerg creep.
*   **power**: Which parts have protoss power, only shows your power.
*   **player_id**: Who owns the units, with absolute ids.
*   **player_relative**: Which units are friendly vs hostile. Takes values in
    [0, 4], denoting [background, self, ally, neutral, enemy] units
    respectively.
*   **unit_type**: A unit type id, which can be looked up in pysc2/lib/units.py.
*   **selected**: Which units are selected.
*   **hit_points**: How many hit points the unit has.
*   **energy**: How much energy the unit has.
*   **shields**: How much shields the unit has. Only for protoss units.
*   **unit_density**: How many units are in this pixel.
*   **unit_density_aa**: An anti-aliased version of unit_density with a maximum
    of 16 per unit per pixel. This gives you sub-pixel unit location and size.
    For example if a unit is exactly 1 pixel diameter, `unit_density` will show
    it in exactly 1 pixel regardless of where in that pixel it is actually
    centered. `unit_density_aa` will instead tell you how much of each pixel is
    covered by the unit. A unit that is smaller than a pixel and centered in the
    pixel will give a value less than the max. A unit with diameter 1 centered
    near the corner of a pixel will give roughly a quarter of its value to each
    of the 4 pixels it covers. If multiple units cover a pixel their proportion
    of the pixel covered will be summed, up to a max of 256.

#### Structured

The game offers a fair amount of structured data which agents aren't expected
to read from pixels. Instead these are given as tensors with direct semantic
meaning.

##### 일반적인 플레이어 정보

A `(11)` tensor showing general information.

*   player_id
*   minerals
*   vespene
*   food used (otherwise known as supply)
*   food cap
*   food used by army
*   food used by workers
*   idle worker count
*   army count
*   warp gate count (for protoss)
*   larva count (for zerg)

##### 제어 그룹

A `(10, 2)` tensor showing the (unit leader type and count) for each of the 10
control groups. The indices in this tensor are referenced by the `control-group`
action.

[Control groups](http://learningsc2.com/tag/control-groups/) are a way to
remember a selection set so that you can recall them easily later.

##### Single Select

A `(7)` tensor showing information about a selected unit.

*   unit type
*   player_relative
*   health
*   shields
*   energy
*   transport slot taken if it's in a transport
*   build progress as a percentage if it's still being built

##### Multi Select

A `(n, 7)` tensor with the same as [single select](#single-select) but for all
`n` selected units. The indices in this tensor are referenced by the
`select_unit` action.

##### Cargo

A `(n, 7)` tensor similar to [single select](#single-select), but for all the
units in a transport. The indices in this tensor are referenced by the `unload`
action.

##### Build Queue

A `(n, 7)` tensor similar to [single select](#single-select), but for all the
units being built by a production building. The indices in this tensor are
referenced by the `build_queue` action.

##### Available Actions

A `(n)` tensor listing all the action ids that are available at the time of this
observation.

##### Last Actions

A `(n)` tensor listing all the action ids that were made successfully since the
last observation. An action that was attempted but failed is not included here.

##### Action Result

A `(n)` tensor (usually size 1) giving the result of the action. The values are
listed in
[error.proto](https://github.com/Blizzard/s2client-proto/blob/master/s2clientprotocol/error.proto)

##### Alerts

A `(n)` tensor (usually empty, occasionally size 1, max 2) for when you're being attacked in a major way.

### Actions

The SC2 action space is very big. There are hundreds of possible actions, many
of which take a point in either screen or minimap space, and many of which take
an additional modifier. If you were to flatten the action space into a single
dimension, it'd have millions or even billions of possible actions, most of
which aren't valid, and many of which are highly correlated. Therefore, a flat
discrete action space is not very appropriate.

Instead, we created function actions that are rich enough to give
composability, without the complexity of an arbitrary hierarchy. This is based
on the mental model of a C-style function call which can take some arguments of
specific types. The full set of valid types and functions are defined in
`ValidActions` in `pysc2.lib.actions`, and then each observation specifies which
of the available function is valid this frame. Each action is a single
`FunctionCall` in `pysc2.lib.actions` with all its arguments filled.

The full set of types and functions are defined in `pysc2.lib.actions`. The set
of functions is hard coded and limited to just the actions that humans have
taken, as seen by a large number of replays. Hard coding the functions means
that actions created in custom maps won't be usable until they are added to
`pysc2.lib.actions`.

The semantic meaning of these actions can mainly be found by searching:
[liquipedia.net/starcraft2](http://liquipedia.net/starcraft2/) or
[starcraft.wikia](http://starcraft.wikia.com/).

#### List of actions

To see which actions exist run:

```shell
$ python -m pysc2.bin.valid_actions
```

optionally with `--hide_specific`, `--screen_resolution` or
`--minimap_resolution` if you care about the exact values. This prints something
similar to:

```
   0/no_op                       ()
   1/move_camera                 (1/minimap [64, 64])
   2/select_point                (6/select_point_act [4]; 0/screen [84, 84])
   3/select_rect                 (7/select_add [2]; 0/screen [84, 84]; 2/screen2 [84, 84])
   4/select_control_group        (4/control_group_act [5]; 5/control_group_id [10])
   5/select_unit                 (8/select_unit_act [4]; 9/select_unit_id [500])
   6/select_idle_worker          (10/select_worker [4])
   7/select_army                 (7/select_add [2])
   8/select_warp_gates           (7/select_add [2])
   9/select_larva                ()
  10/unload                      (12/unload_id [500])
  11/build_queue                 (11/build_queue_id [10])
  12/Attack_screen               (3/queued [2]; 0/screen [84, 84])
  13/Attack_minimap              (3/queued [2]; 1/minimap [64, 64])
  14/Attack_Attack_screen        (3/queued [2]; 0/screen [84, 84])
  19/Scan_Move_screen            (3/queued [2]; 0/screen [84, 84])
  23/Behavior_CloakOff_quick     (3/queued [2])
  26/Behavior_CloakOn_quick      (3/queued [2])
  42/Build_Barracks_screen       (3/queued [2]; 0/screen [84, 84])
  44/Build_CommandCenter_screen  (3/queued [2]; 0/screen [84, 84])
 220/Effect_Repair_screen        (3/queued [2]; 0/screen [84, 84])
 221/Effect_Repair_autocast      ()
 264/Harvest_Gather_screen       (3/queued [2]; 0/screen [84, 84])
 303/Morph_Lair_quick            (3/queued [2])
 317/Morph_SiegeMode_quick       (3/queued [2])
 322/Morph_Unsiege_quick         (3/queued [2])
 331/Move_screen                 (3/queued [2]; 0/screen [84, 84])
 333/Patrol_screen               (3/queued [2]; 0/screen [84, 84])
 405/Research_Stimpack_quick     (3/queued [2])
 451/Smart_screen                (3/queued [2]; 0/screen [84, 84])
 452/Smart_minimap               (3/queued [2]; 1/minimap [64, 64])
 453/Stop_quick                  (3/queued [2])
 477/Train_Marine_quick          (3/queued [2])
           *** 100s more lines ***
```

This should be read as: `<function id>/<function name>(<type id>/<type name>
[<value size>, *]; *)`.

Some examples:

*   `1/move_camera (1/minimap [64, 64])` is the `move_camera` function (id `1`),
    which takes one argument named `minimap` (id `1`) which requires two ints
    each in the range `[0, 64)` which represent the coordinates on the minimap.
*   `331/Move_screen (3/queued [2]; 0/screen [84, 84])` is the `Move_screen`
    function (id `331`) which takes two arguments: `queued` (id `3`) which is a
    bool and signifies whether this action should happen now or after previous
    actions, and `screen` (id `0`) which takes two ints each in the range `[0,
    84)` which represent a pixel on the screen.

The function names should be unique, stable and meaningful. The function and
type ids are the index into the list of `functions` and `types`.

The `types` are a predefined list of argument types that can be used in a
function call. The exact definitions are in `pysc2.lib.actions.TYPES`

#### Action categories

A `Morph` action transform a unit to a different unit, at least according to the
unit_type in the observation. For example `Morph_Lair_quick` morphs a hatchery
to a lair; `Morph_SiegeMode_quick` and `Morph_Unsiege_quick` morphs a siege tank
between tank and siege mode. An `Effect` is a single effect, rarely cancelable.
A `Behavior` can be turned on and off but doesn't change the unit type.

#### General vs Specific actions

StarCraft II speaks in terms of abilities. Sometimes a single concept that can
be done by many units is implemented as a single ability (eg Move, Halt,
Patrol), and sometimes as many abilities (eg Attack, Burrow, Cancel, Lift/Land).
`Burrow` is a simple example where each zerg unit that can burrow has its own
ability (`BurrowDown_Drone`, `BurrowDown_Zergling`, etc). Exposing those
individually would make the action space even more complicated, and make it hard
to burrow a whole army at once given a [limited APM](#apm-and-fairness), so we
added a concept of general abilities that merge all of the specific abilities
that would happen together or using the same key in the game UI. If you give the
specific ability (eg `BurrowDown_Zergling`) it'll only affect the specific units
that support that ability (eg Zerglings), while if you give the corresponding
general ability (`BurrowDown`) it'll affect all units that support it.

Attack is a non-obvious case of this. There is `Attack`, which is the general
ability that corresponds to what the UI does, but under the hood that actually
executes `Attack_Attack` for offensive units, `Scan_Move` for support units like
medivacs that can't attack but should come along as if they can,
`Attack_AttackBuilding` for defensive buildings (eg missile turret) and
`Attack_Redirect` for bunkers to tell their loaded units to attack.

For now only the general actions are exposed through the environment api so only
the general actions should be returned in the available actions observation.

In `pysc2.lib.actions.FUNCTIONS` specific functions have an additional parameter
that references the general parameter.

#### Example usage

Take a look at the [random agent](../pysc2/agents/random_agent.py) for an
example of how to consume `ValidActions` and fill `FunctionCall`s.

The following snippet shows how to print a human-readable list of available
actions:

```python
    from pysc2.lib import actions

    for action in obs.observation.available_actions:
        print(actions.FUNCTIONS[action])
```

## RL Environment

The main SC2 environment is at `pysc2.env.sc2_env`, with the action and
observation space defined in `pysc2.lib.features`.

The most important argument is `map_name`, which is how to find the map.
Find the names by using `pysc2.bin.map_list` or by looking in `pysc2/maps/*.py`.

`players` lets your specify the number and type of players. At the moment only
one or two players are supported. Give it a list of `sc2_env.Agent` or
`sc2_env.Bot` objects, specifying the race and difficulty. Specifying two agents
will start up two instances of SC2 which communicate between themselves, and
consume double the memory and cpu as playing single player.

`agent_interface_format` lets you specify the observation and action interface
to be used by each agent. `feature_dimensions` and `rgb_dimensions` let you
specify the resolution of the spatial observations. Higher resolution obviously
gives higher location precision, at the cost of larger observations as well as a
larger action space, and slower rendering time.

If you ask for both feature and rgb observations you'll need to specify the
action space that you want to use. This lets you act in one while learning from
the other.

`step_mul` let's you skip observations and actions. For example a `step_mul` of
16 means that the environment gets stepped forward 16 times in between the
actions of the agent (16 steps = 1 second of game time). It is equivalent to
ignoring certain observations and not sending actions on those frames, except it
also speeds up the environment since it doesn't need to render the skipped
frames.

`save_replay_episodes` and `replay_dir` specify how often to save replays and
where to save them.

Use the `run_loop.py` to have your agent interact with the environment.

### Environment wrappers

There is one pre-made environment wrapper:

*   `available_actions_printer`: Prints each available action as it is seen.

## Agents

There are a couple basic agents.

*   `random_agent`: Just plays randomly, shows how to make valid moves.
*   `scripted_agent`: These are scripted for a single mini game.
