# Console Commands

## Commands

### 3dstats

* **Description**: Toggles 3D Stats

### AddFunds

* **Description**: "Add funds to one or all Military Industrial Organisations
ex:
AddFunds org_token 2000
AddFunds org_token // default added funds is NDefines::NIndustrialOrganisation::FUNDS_FOR_SIZE_UP
AddFunds 2000 // Funds added to all the player's MIOs
AddFunds // default funds amount added to all the player's MIOs"
* **Aliases**: mio.AddFunds, IndustrialOrganisation.AddFunds
* **Arguments**: `<Industrial Organisation token> (optional) <Funds amount> (optional)`

### AddSize

* **Description**: "Add sizes to one or all Military Industrial Organisations.
ex:
AddSize org_token 2
AddSize org_token // adds 1 size
AddSize 2 // adds input size to all the player's MIOs
AddSize // adds 1 size to all the player's MIOs"
* **Aliases**: mio.AddSize, IndustrialOrganisation.AddSize
* **Arguments**: `<Industrial Organisation token> (optional) <capacity amount> (optional)`

### AddTaskCapacity

* **Description**: "Add task capacity to one or all Military Industrial Organisations.
Value can be negative but final task capacity will be capped at 0.
ex:
AddTaskCapacity org_token 2
AddTaskCapacity org_token // adds 1 capacity
AddTaskCapacity 2 // adds input capacity to all the player's MIOs
AddTaskCapacity // adds 1 capacity to all the player's MIOs"
* **Aliases**: mio.AddTaskCapacity, IndustrialOrganisation.AddTaskCapacity
* **Arguments**: `<Industrial Organisation token> (optional) <capacity amount> (optional)`

### Agency.Instant

* **Description**: Activates Operation.Instant, IntelNetwork.Instant, Agency.InstantSlotUnlock and Agency.Autocomplete

### Audio.PlayEffect

* **Description**: Play the specified sound effect
* **Arguments**: `effect_name`

### CrashReporter.DeleteCrashData

* **Description**: Delete local crash dumps older than X days.

### CrashReporter.SimulateCrash

* **Description**: Simulates a crash (resulting in the game exiting).

### IP

* **Description**: Shows your IP

### InternationalMarket.AddSubsidyForTags

* **Description**: Add a Equipment Subsidy to the player's international market.
* **Arguments**: `<CIC> <Archetype> <Tag>`

### InternationalMarket.AddSubsidyForTrigger

* **Description**: Add a Equipment Subsidy to the player's international market.
* **Arguments**: `<CIC> <Archetype> <ScriptedTrigger> `

### InternationalMarket.CancelPurchase

* **Description**: Cancel the purchase contract between the seller and the buyer
* **Arguments**: `<SellerTag> <BuyerTag> <ContractIndex>`

### InternationalMarket.Dev.SetMarketRequestAutomation

* **Description**: Set the market requests automation state
* **Arguments**: `<AcceptMarketAccess> <SendMarketAccess> <AcceptPurchase>`

### InternationalMarket.ReleaseFromMarketStockpile

* **Description**: Release equipment to main stockpile from market stockpile
* **Arguments**: `<EquipmentName> <EquipmentAmount>`

### InternationalMarket.RequestPurchase

* **Description**: Request Equipment Purchase.
* **Arguments**: `<SellerTag> <BuyerTag> <PaidCivs> <EquipmentName> <EquipmentAmount>`

### InternationalMarket.ReserveToMarketStockpile

* **Description**: Reserve equipment from main stockpile to market stockpile
* **Arguments**: `<EquipmentName> <EquipmentAmount>`

### InternationalMarket.SetPriceLevel

* **Description**: Sets the price level for the given equipment in the Market Stockpile
* **Arguments**: `<EquipmentName> <Level>`

### ListIncorrectCenterOfRegions

* **Description**: List regions center point that is located within another region

### PopsFileStorage.Sync

* **Description**: Sync POP File Storage

### PostEffectVolumes.Default

* **Description**: Toggles default posteffect values
* **Arguments**: `posteffect_values name`

### PrintSynchStuff

* **Description**: Prints random count and seed

### SetRandomCount

* **Description**: Sets the randomcount to 0 or arg

### acclimatization

* **Description**: Sets the acclimatization on a division(s).
* **Aliases**: acc
* **Arguments**: `<climate_name> <value 0-100>`

### add_autonomy

* **Description**: Adds the specified amount of autonomy to a country.
* **Arguments**: `<country_tag> <value>`

### add_cic_bank

* **Description**: Add CIC to the CIC bank (negative value subtracts)
* **Aliases**: stonks, cic, bank
* **Arguments**: `<value>`

### add_core

* **Description**: Add core
* **Arguments**: `<Province ID>`

### add_critical_hit

* **Description**: add critical hit to selected ships
* **Arguments**: `<critical_hit_name>`

### add_diplo

* **Description**: Adds diplomatic entroute

### add_equipment

* **Description**: Gives player amount of equipment that has the specified name
* **Aliases**: ae
* **Arguments**: `equipment amount equipment name`

### add_exile_manpower

* **Description**: Adds legitimacy to specified tag. add_legitimacy TAG amount
* **Arguments**: `<TAG> <value>`

### add_fake_armies

* **Description**: Creates fake intel armies for the player

### add_fleet_arrow

* **Description**: Add an arrow around a strategic region
* **Arguments**: `color`

### add_ideas

* **Description**: Adds ideas (ministers or national spirits) with <ID> to the country. Use 'all' to add them all
* **Arguments**: `all|<idea1> <idea2> ...>`

### add_intel

* **Description**: Set the values of a static intel pool against a specific country. E.g. `add_intel GER POL army=10`

### add_latest_equipment

* **Description**: Gives player amount of latest equipment variants
* **Aliases**: ale
* **Arguments**: `equipment amount`

### add_legitimacy

* **Description**: Adds legitimacy to specified tag. add_legitimacy TAG amount
* **Arguments**: `<TAG> <value>`

### add_mines

* **Description**: Add naval mines to selected region(s)
* **Aliases**: mines
* **Arguments**: `<Amount of naval mines>`

### add_opinion

* **Description**: Add opinion to/from tag
* **Arguments**: `<Country tag>`

### add_party_popularity

* **Description**: Adds party popularity for specified party to the current country
* **Arguments**: `<party> <amount>`

### add_rain

* **Description**: Adds rain to the selected province
* **Arguments**: `<rain_amount>`

### add_snow

* **Description**: Adds snow to the selected province
* **Arguments**: `<snow_amount>`

### add_stability

* **Description**: Gives/removes stability from player
* **Aliases**: st
* **Arguments**: `unity amount`

### add_subsidies


### add_subsidies_second


### add_tech

* **Description**: Adds the specified technology to the player's country.
* **Arguments**: `<technology_key>`

### add_temp_supply_node

* **Description**: Add temp supply node

### add_temporary_buff

* **Description**: adds temporary buff to selected units
* **Arguments**: `<buff_index>`

### add_war_support

* **Description**: Gives/removes war support from player
* **Aliases**: ws
* **Arguments**: `unity amount`

### ai

* **Description**: Toggles the AI on or off

### ai_accept

* **Description**: Toggles AI always accept diplomacy
* **Aliases**: yesman

### ai_dump

* **Description**: Dump AI data to log file
* **Aliases**: aidump

### ai_force_equipment

* **Description**: Force the AI to only spend army XP on equipment design

### ai_force_template

* **Description**: Force the AI to only spend army XP on template design

### ai_front_dump

* **Description**: Dump AI front data to log file, needs to have a unit selected
* **Aliases**: aifrontdump

### ai_front_id

* **Description**: Get the address of selected group's front debug id

### ai_idea_desire_log

* **Description**: Prints AI desire for ideas to log. For Current country only.

### ai_invasion

* **Description**: Toggles AI AI naval invasions

### ai_pp_log

* **Description**: Prints AI use of PP to log

### ai_research_log

* **Description**: Toggles ai research logging

### ai_trace

* **Description**: Toggles the AI Trace window

### aircombat

* **Description**: Spawns an air combat in desired location.
* **Aliases**: airc
* **Arguments**: `<scenario name> <result name> <province id> <state id with airbase> <state id with airbase> <equipment type> <equipment type> [equipment creator country] [equipment creator country]`

### airealism

* **Description**: Enable realistic AI

### aiview

* **Description**: Enable AI debug info

### allowdiplo

* **Description**: Allows to use all diplomatic actions for no matter the rules.
* **Aliases**: adiplo, nocb

### allowideas

* **Description**: Allows to learn all ideas.

### allowoperations

* **Description**: Allows to execute all operations.

### allowtraits

* **Description**: Allows to learn all traits.

### analyzetheatres

* **Description**: Analyze theatres for errors.
* **Aliases**: anth

### annex

* **Description**: Begin annex/annexes the specified tag
* **Arguments**: `<Target Country Tag>`

### armageddon

* **Description**: Deliver a thermonuclear strike to every state in the game.

### bloom

* **Description**: Toggles bloom

### bop_add

* **Description**: Changes the value of the specified power balance.
* **Arguments**: `<ID> <value>`

### bop_addmod

* **Description**: Adds static modifier to a power balance.
* **Arguments**: `<ID> <ModID>`

### bop_remove

* **Description**: Deactivates a power balance for the current country.
* **Arguments**: `<ID>`

### bop_rmmod

* **Description**: Removes static modifier from a power balance.
* **Arguments**: `<ID> <ModID>`

### bop_set

* **Description**: Activates a power balance for the current country.
* **Arguments**: `<ID>`

### bop_show

* **Description**: Shows current country's active power balances.

### browser

* **Description**: Show browser window
* **Arguments**: `url`

### build_war_blobs

* **Description**: Prints a list of all your wars

### building_health

* **Description**: Changes specified building health
* **Aliases**: bhealth
* **Arguments**: `<building type> <state or prov id> <building level> <health to add>`

### bypass_invasion_superiority_check

* **Description**: Ignore superiority in the strategic areas crossed by a naval invasion order
* **Aliases**: bisc

### cameraclamp

* **Description**: Toggles the camera clamping

### cityreload

* **Description**: Reloads the cities

### civilwar

* **Description**: Spawns a civil war
* **Arguments**: `<ideology> [target country tag]`

### clear_critical_hits

* **Description**: clear all critical hits

### clear_intel_pools

* **Description**: Reset the specified intel pool

### clear_tech

* **Description**: Removes all researched technologies for the player's country.

### collaboration

* **Description**: Adds collaborations against selected country. Right click to select a country and use "collaboration 0.3"

### collision

* **Description**: Toggles debug display of normals/bounding boxes/collision
* **Aliases**: debug_collision

### combat_analyzer

* **Description**: Runs a combat between the 2 OOBs owned by the two TAGs either until done or for the specified number of days. 
Using <num runs> the combat will be run multiple times and the averages are printed
* **Arguments**: `<TAG1> <TAG2> <OOB1> <OOB2> <num runs> OPTIONAL <num days> OPTIONAL`

### combatsound

* **Description**: How often does the combat view give a random sound? 0-50

### combattest

* **Description**: combat simulation process

### compare_to_last_checksum

* **Description**: Compare current checksum with the most recent dump

### compliance

* **Description**: increases decreases compliance in a state
* **Arguments**: `amount`

### cp

* **Description**: Gives command power to player
* **Arguments**: `CP amount`

### createarmygroup

* **Description**: Create field marshal group from selected groups

### createlean

* **Description**: Create LEAN textures

### ct

* **Description**: Puts timer info in clipboard

### damage_units

* **Description**: Damage or heal selected units or units under pointer if there is none selected. Enter 1 argument to apply damage for both types, two for individual both types
* **Arguments**: `<org> <str> <num>`

### dbg_enable_scripted_gui

* **Description**: Enables scripted GUIs
* **Arguments**: `<scope>`

### dbg_prov

* **Description**: Sets type of debugging information on provinces.
* **Arguments**: `<int>`

### dbg_task_force_role_insignia_assignment

* **Description**: print the role that would be deduced for the selected task force
* **Aliases**: tfria

### dbg_tf_fulfillment

* **Description**: Show the managed fulfillment of a taskforce (exepected number of ships after all ships have been merged in)

### debug

* **Description**: Toggle debug mode on/off.

### debug_achievements

* **Description**: Enables popups for achievements to debug them

### debug_achievements_clear

* **Description**: Clear all achievements and user stats

### debug_air_vs_land

* **Description**: Toggle debug mode for air vs land combat.
* **Aliases**: dbg_cas

### debug_army_entity

* **Description**: Shows debug entity for all armies
* **Aliases**: dae

### debug_assert

* **Description**: Toggles asserts on/off

### debug_bloom

* **Description**: Toggles Bloom on/off

### debug_borders

* **Description**: Toggles Borders on/off

### debug_checkportraitssanity

* **Description**: Analyse all characters' portraits and write failures in error log

### debug_cities

* **Description**: Toggles Cities painting mode on/off

### debug_commands

* **Description**: Printing commandcount to message.log

### debug_crash

* **Description**: Crash!
* **Aliases**: crash

### debug_custom_achievements

* **Description**: For testing custom achievements, clear completion status (delete files on cloud storage) and reload mod achievement files

### debug_diploactions

* **Description**: Start Counting diplomatic actions

### debug_dumpdiploactions

* **Description**: Dump diplomatic action data to game log

### debug_dumpevents

* **Description**: Dump Event data to game log

### debug_entities

* **Description**: Toggles Debug entities

### debug_events

* **Description**: Start Counting events

### debug_force_capitulate

* **Description**: forces capitulation of a country on next daily tick
* **Aliases**: dfc
* **Arguments**: `<tag>`

### debug_front_sections

* **Description**: Visual debug of theatres, fronts and sections.
* **Aliases**: dbg_fs
* **Arguments**: `<Theatre index> <Front index> <Section index>`

### debug_fronts

* **Description**: Toggles interpolated fronts debug

### debug_info

* **Description**: Toggles Debug info

### debug_lines

* **Description**: Toggles Debuglines

### debug_lockcamera

* **Description**: Toggles Camera locked on/off

### debug_nogui

* **Description**: Toggles GUI on/off

### debug_nomouse

* **Description**: Toggles mouse scrollwheel on/off

### debug_norender

* **Description**: Toggle rendering of map

### debug_off_front_snap

* **Description**: Toggles offensive fronts snapping debug
* **Aliases**: dbg_fsnap

### debug_orders_tree

* **Description**: Print out debug about orders chain.
* **Aliases**: dot

### debug_particle

* **Description**: Toggles Particles Debug info

### debug_postfx

* **Description**: Toggles PostFX on/off

### debug_rivers

* **Description**: Toggles Rivers on/off

### debug_show_event_ID

* **Description**: Shows event ID

### debug_sky

* **Description**: Toggles Sky on/off

### debug_smooth

* **Description**: Toggle framesmoothing

### debug_tactics

* **Description**: Toggle visibility of debug tooltip for tactics

### debug_terrain

* **Description**: Toggles Terrain on/off

### debug_texture

* **Description**: draws textures like bloom

### debug_textures

* **Description**: Writes Texture info to application debug log

### debug_tooltip

* **Description**: Toggles Tooltips on/off

### debug_trees

* **Description**: Toggles Trees on/off

### debug_types

* **Description**: Will print the data type for all dynamic reference objects. Can only be used if using RTTI.

### debug_unit_controller_weights

* **Description**: Visual debug of unit controller weights. Enable track_unit_controller_weights first!
* **Aliases**: dbg_ucw
* **Arguments**: `<weight token>`

### debug_unit_entity

* **Description**: Print out the entity hierarchy.
* **Aliases**: dbg_ue

### debug_validate_supply

* **Description**: Toggle debug validate supply cache.
* **Aliases**: dbg_sply

### debug_water

* **Description**: Toggles Water on/off

### debug_wireframe

* **Description**: Toggles forced wireframe on/off

### debug_zoom

* **Description**: Zooms in the game

### deironman

* **Description**: Removes Ironman status from current game.

### deleteallairwings

* **Description**: Delete all airwings.
* **Aliases**: delallair

### deleteallunits

* **Description**: Delete all armies and fleets of the specified countries.
* **Aliases**: delall

### deleteallunitsbut

* **Description**: Delete all armies and fleets of ALL countries, except specified one.
* **Aliases**: delallbut

### deltat

* **Description**: control animation speeds
* **Arguments**: `<speed factor>`

### disable_ai

* **Description**: Disables the AI

### disable_weather

* **Description**: Disable weather simulation

### drop_cosmetic_tag

* **Description**: Drops 'cosmetic tag' for a specified country
* **Arguments**: `<country tag>`

### dump_cached_random_logs

* **Description**: dumps cached random logs

### dump_checksum

* **Description**: Compute and store the checksum in a file

### dump_equipment_loc

* **Description**: Dumps equipment loc strings to file. All arguments are optional.
* **Arguments**: `desc: Dump equipment descriptions instead of the names <country_tag>: Multiple allowed. Only include loc strings for the given countries. Generic loc strings are included if no tags are given, or with argument 'generic'. <type>: Multiple allowed. Only include equipment that are all of the given types, e.g. 'armor anti_tank' will only include tank destroyers. path=<filepath>: File path to write the dump to. Default is 'logs/equipment_loc.csv'.`

### dump_garrison_templates

* **Description**: Dump garrison templates to game log

### dump_synchronized_members

* **Description**: Dump the synchronized game state (the one that has checksum ID 2)

### easy_decisions

* **Description**: Toggles Easy Decisions Mode which makes all decisions with days_remove take only 1 day to be removed, and all decisions with cost not have any cost or cost trigger.
* **Aliases**: ezd

### effect

* **Description**: Runs a scripted effect on selected scope
* **Aliases**: e
* **Arguments**: `<tag> scripted_effect_name`

### empty_fuel_tanks

* **Description**: Clear fuel tanks of all armies
* **Arguments**: `Fuel amount`

### emulate_ai_operative_assignment

* **Description**: Log ai operative assignment if it were to run this tick. Takes as first argument the tag of the country to test, default to the player's.

### enable_ai

* **Description**: Enables the AI

### enable_weather

* **Description**: Enable weather simulation

### endraids

* **Description**: Instantly end all active raids, optionally with a specific success level
* **Arguments**: ` <Success Level: 1-4 OR { failure, limitedsuccess, success, criticalsuccess}>`

### error

* **Description**: Show errors in log

### eval_effect

* **Description**: Runs the inlined effect on a selected scope

### eval_trigger

* **Description**: Runs the inlined trigger on a selected scope

### event

* **Description**: Executes an event
* **Arguments**: `event id <Target Country Tag>`

### flagsoutput

* **Description**: Creates texture atlas files from memory.
* **Arguments**: `<path>`

### focus_count

* **Description**: Counts how many focuses a tag has. For science
* **Arguments**: `<Target Country Tag>`

### force_operative_detection

* **Description**: Print intel network related information
* **Aliases**: snitch

### forget_medals_and_ribbons

* **Description**: Make the game forget that you have earned medals and ribbons.

### fow

* **Description**: Turns off fog of war in a province or in general
* **Aliases**: debug_fow
* **Arguments**: `<Province ID> OPTIONAL`

### freefocuses

* **Description**: Enable freely activating any focuses
* **Aliases**: ff

### fronts

* **Description**: Toggle visibility of the foreign fronts

### fuel

* **Description**: Adds/removes fuel to the player
* **Aliases**: army_juice
* **Arguments**: `Fuel amount`

### fuel_gain

* **Description**: Adds/removes daily fuel gain for player
* **Arguments**: `Daily Fuel amount`

### fullscreen

* **Description**: Toggles fullscreen

### gain_xp

* **Description**: Gain xp for selected leader or for a leader trait
* **Arguments**: `<trait>`

### gamespeed

* **Description**: Set the current game speed, pausing the game at speed 0.
* **Arguments**: `speed <0-5>`

### gamestate_timer

* **Description**: Enable / Disable recording of how long an hour / day / week etc takes to process.
* **Aliases**: gstimer
* **Arguments**: `on / off`

### gbpaint

* **Description**: Toggles gradient border painting
* **Arguments**: `layer channel`

### gbreload

* **Description**: Reloads gradient borders

### get_capital

* **Description**: Get the capital of a country
* **Arguments**: `<Country tag>`

### get_country_flag

* **Description**: Gets country flag on specified TAG. Defaults to current country
* **Arguments**: `<flag name>`

### get_flag

* **Description**: Get a flag
* **Arguments**: `<flag name>`

### get_var

* **Description**: Gets a variable
* **Arguments**: `<var name>`

### goto_province

* **Description**: Centers to province
* **Arguments**: `province id`

### goto_region

* **Description**: Centers to region
* **Arguments**: `region id`

### goto_state

* **Description**: Centers to state
* **Arguments**: `state id`

### grow_intel_network

* **Description**: Grow the intel network in the specified tag

### guibounds

* **Description**: Toggles GUI bounds debug
* **Aliases**: gui

### hdr

* **Description**: Toggles hdr

### hdr_debug

* **Description**: Toggles hdr debugging

### help

* **Description**: Print out all console commands or a specific command description.
* **Arguments**: `command name`

### helphelp

* **Description**: Double Rainbow help.

### helplog

* **Description**: Print out all console commands to game.log file.

### highlight_encirclements

* **Description**: Toggle highlighting of detected encirclements

### history_logger

* **Description**: Toggle history logger

### hsv

* **Description**: Converts RGB to HSV

### human_ai

* **Description**: Toggles AI for Human countries

### imgui

* **Description**: Controls ImGui UIs. See the sub commands.

### instant_prepare

* **Description**: Instantly prepares naval invasions

### instant_wargoal

* **Description**: Generation of wargoals are instant

### instantconstruction

* **Description**: Toggles instant construction cheat.
* **Aliases**: ic

### instantevents

* **Description**: Ignores event mth s

### instantshiprefit

* **Description**: Toggles instant ship refitting cheat.
* **Aliases**: isr

### instanttraining

* **Description**: Toggles instant army training cheat.
* **Aliases**: it

### ironman

* **Description**: Applies Ironman status to current game.

### launch_nuke

* **Description**: Launch nuke to any specified province(s) without checking any conditions.
* **Aliases**: ln
* **Arguments**: `[Nuke Type] <Province ID> ...`

### list_flags

* **Description**: Lists all flags in a scope or for the selected country/state/unitleader
* **Arguments**: `<scope>`

### list_ideas

* **Description**: Dump all ideas to console (ministers or national spirits)

### list_modifiers

* **Description**: Lists all modifiers in a scope or for the selected country/state/unitleader
* **Arguments**: `<scope>`

### list_temporary_buffs

* **Description**: lists all temporary buffs on selected units

### list_vars

* **Description**: Lists all variables in a scope or for the selected country/state/unitleader
* **Arguments**: `<scope>`

### loc_check

* **Description**: Check for missing localization

### loc_check_characters

* **Description**: Check characters for missing localization

### loc_check_decisions

* **Description**: Check decisions for missing localization

### loc_check_events

* **Description**: Check events for missing localization

### loc_check_focuses

* **Description**: Check national focuses for missing localization

### loc_check_modifiers

* **Description**: Check modifiers for missing localization

### loc_check_national_spirits

* **Description**: Check national spirits for missing localization

### lock_air_det

* **Description**: Locks Air Detection for a country, omit detection value to reset
* **Arguments**: `<CountryTag> <Detection> (0.0-1.0) OPTIONAL`

### lock_air_eff

* **Description**: Locks Air Efficiency for a country, omit efficiency value to reset
* **Arguments**: `<CountryTag> <Efficiency> (0.0-1.0) OPTIONAL`

### log_advisor_trait_errors

* **Description**: Logs all instances of unit leader advisors not having the corresponding unit leader traits.

### manpower

* **Description**: Adds manpower to player
* **Arguments**: `<Amount>`

### map_icon_reload_type

* **Description**: Specify a map icon type to reload
* **Arguments**: `<NUM> or <help>`

### mapmode

* **Description**: Change mapmode.
* **Arguments**: `Mapmode type (int)`

### mapnames

* **Description**: Toggle map names

### massconquer

* **Description**: Mass conquer tool.
* **Aliases**: massc

### metrics

* **Description**: Toggles collecting metrics
* **Arguments**: `log_units|log_pools|player|air_mission|global|unit_assignments <days>|decision|log|file<=file_name>|tag=<country_tag>|add_tag=<country_tag>`

### morehumans

* **Description**: Adds more humans
* **Aliases**: humans
* **Arguments**: `num`

### morehumanswithcountries

* **Description**: Adds more humans and assigns them to the highest scoring countries available
* **Arguments**: `num`

### moveunit

* **Description**: Moves a unit to a province
* **Arguments**: `<Unit ID> <Province ID>`

### navalcombatlog

* **Description**: logs naval combat

### night

* **Description**: Toggles night

### no_wargoal

* **Description**: No need to have a wargoal for declaring war

### nomapicons

* **Description**: Toggles map icons.

### nopausetext

* **Description**: Toggles the pausebanner for nicer screenshots.

### nudge

* **Description**: Go to the nudge tool

### nukes

* **Description**: add nukes
* **Aliases**: nuke
* **Arguments**: `<count>`

### observe

* **Description**: Switches to play no country at all, and no longer shows messages or pauses the game
* **Aliases**: spectator

### occupationpaint

* **Description**: Toggles occupation painting. If specifying a tag, that country will be occupied.
* **Aliases**: op
* **Arguments**: `tag<OPTIONAL>`

### oos

* **Description**: Out of Synch

### oos_dump

* **Description**: Generates an oos dump on demand for local client.
* **Aliases**: oosdump

### operation_debug

* **Description**: Allows to execute all operations.
* **Arguments**: `Operation ID Target Tag`

### operation_start

* **Description**: Allows to execute all operations.
* **Arguments**: `Operation ID Target Tag`

### operation_test_phase_selection

* **Description**: Test an operation phase.
* **Arguments**: `Operation ID Target Tag`

### pathfind_cache

* **Description**: Enable / Disable the PathFind Cache
* **Arguments**: `on / off`

### pathfind_stats

* **Description**: Print PathFind Cache Stats

### pause_in_hours

* **Description**: Pauses the game after X hours have passed after command is called

### pause_on_trigger

* **Description**: Pauses the game when trigger activates

### pops_account_disconnect_steam

* **Description**: Disconnect Paradox account from Steam

### pops_account_login

* **Description**: Login to a POPS Account
* **Arguments**: `email password`

### pops_account_logout

* **Description**: Login to a POPS Account

### pops_account_status

* **Description**: Show whether you are currently logged into POPS or not.

### pp

* **Description**: Gives political power to player
* **Aliases**: political_power
* **Arguments**: `PP amount`

### prep_for_war

* **Description**: Make AI country with specified TAG to prepare fight for another country 
* **Arguments**: `<TAG>`

### prepareraids

* **Description**: Instantly complete preparation of all active raids, optionally to a specific progress level
* **Arguments**: ` <[Optional] the degree to which the raid should be prepared (0.0-1.0)>`

### prevent_operative_detection

* **Description**: Prevent a country from detecting and harming foreign operatives

### prices

* **Description**: Price Info

### print_controllers

* **Description**: Prints countries controlled by human players.

### print_intel_network

* **Description**: Print intel network related information

### print_intel_values

* **Description**: Print the intel a country has over another

### print_operation_tokens

* **Description**: Runs a scripted effect on selected scope

### print_radar_intel

* **Description**: Print the intel value breakdown generated by radar

### profile

* **Description**: profile options
* **Arguments**: `<on> <off> <print> <clear>`

### province_ids

* **Description**: Show province IDs on the map
* **Aliases**: pid

### provtooltipdebug

* **Description**: Toggles the debug info in province tooltip
* **Aliases**: tdebug

### puppet

* **Description**: Puppets the specified tag
* **Arguments**: `<Target Country Tag>`

### railroads

* **Description**: Toggle rendering of railroads

### railwaygun

* **Description**: create railway gun in supply capital
* **Aliases**: rg

### railwaygun_damage

* **Description**: damage railway guns
* **Aliases**: rg_damage

### random_seed

* **Description**: reseeds random with specified seed or reseeds random

### randomlog

* **Description**: Toggles the random logs.
* **Aliases**: rlog

### rebuildfronts

* **Description**: Rebuild fronts.
* **Arguments**: `<Country tag>`

### rebuildlayers

* **Description**: Reload mapmodes.

### release

* **Description**: Released a given country
* **Aliases**: rls
* **Arguments**: `Tag of a country to be released`

### reload_textures

* **Description**: Reloads all textures, with an optional filter to reload only files that include the given text
* **Aliases**: rt, reload_texture
* **Arguments**: `<optional file name filters...>`

### reloadfx

* **Description**: Reloads the shader
* **Arguments**: `Arguments: map/mapname/postfx or *.fx filename`

### reloadinterface

* **Description**: Reloads the entire interface

### reloadoob

* **Description**: Reloads OOBs
* **Arguments**: `<Target Country Tag>`

### reloadtechnologies

* **Description**: Reloads the technology database

### reloadweather

* **Description**: Reload and regenerate weather
* **Arguments**: `<randomseed>`

### remove_core

* **Description**: Remove core
* **Arguments**: `<Province ID>`

### remove_ideas

* **Description**: Removes ideas (ministers or national spirits) with <ID> to the country. Use 'all' to remove them all
* **Arguments**: `all|<idea1> <idea2> ...`

### research

* **Description**: Researches an technology from research slot or all.
* **Arguments**: `<slot id> or "all"`

### research_fast

* **Description**: Base cost of every technology is set to 1 RP

### research_on_icon_click

* **Description**: Research a technology when clicking on technology tree icon
* **Aliases**: roic

### resign

* **Description**: Resign from the game

### resistance

* **Description**: increases decreases resistance in a state
* **Arguments**: `amount`

### restart

* **Description**: Restart the game as the current country

### retire_country_leader

* **Description**: Retires the current country's leader.

### run

* **Description**: Runs the specified file with list of commands

### savecheck

* **Description**: Makes a savegame (Test_01), loads the savegame, makes a new savegame (Test_02). Those savegames should look the same.

### savegame

* **Description**: Creates a save file.
* **Aliases**: save

### select

* **Description**: select object by id
* **Aliases**: sel
* **Arguments**: `<object id> <object type id> (optional)`

### set_cosmetic_tag

* **Description**: Sets 'cosmetic tag' for a specified country
* **Arguments**: `<country tag> <cosmetic tag>`

### set_country_flag

* **Description**: Sets country flag on specified TAG for a duration. Defaults to current country and value 1 with infinite duration.
* **Arguments**: `<flag name>`

### set_debug_unit_controller

* **Description**: Sets debug unit controller tag, other countries will not update units
* **Aliases**: dbg_unit_controller

### set_flag

* **Description**: Set a flag
* **Arguments**: `<flag name>`

### set_global_flag

* **Description**: Sets the specified global flag to a value. Defaults to 1
* **Arguments**: `<flag name>`

### set_mud

* **Description**: Sets mud for the selected province

### set_ruling_party

* **Description**: Sets ruling party for the country
* **Arguments**: `<ideology>`

### set_var

* **Description**: Set a variable
* **Arguments**: `<var name>`

### set_weather

* **Description**: Sets the weather for the selected province (and corresponding region)
* **Arguments**: `<weather_type>`

### setcontroller

* **Description**: Sets province controller
* **Arguments**: `country tag province id`

### setowner

* **Description**: Sets state owner
* **Arguments**: `country tag state id`

### show_all_medals

* **Description**: Show all medals as achieved in the grid without actually earning them.
* **Arguments**: `<bronze|silver|gold>`

### show_all_ribbons

* **Description**: Show all ribbons as achieved in the grid without actually earning them.

### show_enemy_ships

* **Description**: Toggle always showing of enemy ships

### show_medal

* **Description**: Show the popup for earning a medal without actually earning it.
* **Arguments**: `<medal_token> <bronze|silver|gold>`

### show_ribbon

* **Description**: Show the popup for earning a ribbon without actually earning it.
* **Arguments**: `<ribbon_token>`

### show_ships

* **Description**: Toggle always showing of player ships

### show_xp_gain

* **Description**: Show XP gain information.
* **Aliases**: xp_gain

### simplified_transport

* **Description**: Toggle simplified naval transports

### sleep

* **Description**: Sleep
* **Aliases**: wait
* **Arguments**: `time in sec`

### social_addfriend

* **Description**: Add a friend to friends list
* **Arguments**: `Context Index Account ID`

### social_debuginfo

* **Description**: Print debug info about the social layer

### social_joinroom

* **Description**: Join a chat room using the given social context
* **Arguments**: `Context Index Room Name Nick Name`

### social_sendmessage

* **Description**: Send a message to a chat room.
* **Arguments**: `Context Index Room Name Message`

### sp_add_mastermind

* **Description**: "Add a scientist with max skill in all specializations"

### sp_add_scientist

* **Description**: "Add a scientist. Is specified a specialization and level that will be applied to the scientist. If no specialization is specified the level will be applied to all.
ex:
sp_add_scientist 3 nuclear
sp_add_scientist 2
sp_add_scientist"
* **Arguments**: `<Level> (optional) <Specialization> (optional)`

### sp_add_selected_scientist_level

* **Description**: "Add level and if specified, specifically to a specialization for a scientist. If no specialization is specified, the level will be added for each specialization. Requires the facility view with an attached scientist to be open.
ex:
sp_add_scientist_level 3 nuclear
sp_add_scientist_level 2"
* **Arguments**: `<Level> <Specialization> (optional)`

### sp_add_selected_scientist_trait

* **Description**: "Add a trait to the scientist. Requires the facility view with an attached scientist to be open.
ex:
sp_add_scientist_trait my_trait_token"
* **Arguments**: `<Trait>`

### sp_available

* **Description**: "Trigger available returns true for all Special Projects.
ex:
sp_available"

### sp_breakthrough

* **Description**: "Create breakthrough points."
* **Aliases**: sp_br
* **Arguments**: `<amount> optional <specialization>`

### sp_fast

* **Description**: "All phases in Special Projects take now 1 day to complete.
For prototype phase, it's the iterations that will take 1 day. And it will require as many iterations as usual.
ex:
sp_fast"

### sp_instant

* **Description**: "All started Special Projects finish on the daily tick. It skips the iterations of the Prototyping phase and their reward.
ex:
sp_instant"

### sp_prototype_reward

* **Description**: "Trigger a specified prototype reward during a project."
* **Aliases**: spr
* **Arguments**: ``

### sp_remove_selected_scientist_trait

* **Description**: "Remove a trait from the scientist. Requires the facility view with an attached scientist to be open.
ex:
sp_remove_selected_scientist_trait my_trait_token"

### sp_research_all

* **Description**: "Research all special projects. If no scientist exist it will create one, otherwise it will pick an arbitrary one. Imagine there is a secret hidden facility
in a controlled province where the projects are researched."
* **Aliases**: sp_ra

### sp_set_selected_scientist_level

* **Description**: "Set level and if specified, specifically to a specialization for a scientist. If no specialization is specified, the level will be added for each specialization. Requires the facility view with an attached scientist to be open.
ex:
sp_set_scientist_level 3 nuclear
sp_set_scientist_level 2"
* **Arguments**: `<Level> <Specialization> (optional)`

### sp_unlock_all

* **Description**: "All Special Projects are always visible and available. Whether or not the triggers returns true, and whether the parents are completed.
ex:
sp_unlock_all"

### spawn

* **Description**: Spawns a unit in a province
* **Arguments**: `<SubUnit Type> <Province ID> <Amount>`

### spawn_3D_models


### spawnactor

* **Description**: Spawns an actor with an optional animation
* **Arguments**: `<Actorname> <Province ID> <Animation> OPTIONAL`

### srgb

* **Description**: Toggles sRGB

### supply_toggle_flow_penalties

* **Description**: Toggle the supply penalties due to bad supply flow

### tag

* **Description**: Switch tag to another country
* **Arguments**: `<Country tag>`

### tag_color

* **Description**: Test setting a country's color

### teleport

* **Description**: Teleports selected armies or ships to the specified province
* **Aliases**: tp
* **Arguments**: `<province_id>`

### test

* **Description**: This is a placeholder command. Use it for your debug code if you need to quickly test something locally. Or copy and paste it to create a new console command.

### test_log

* **Description**: Enable / Disable tests

### test_naval_move_danger

* **Description**: Tests if path between two regions is blocked for surface warships
* **Arguments**: `<from region id> <to region id>`

### test_save_mode

* **Description**: Sets if save game for failed test should be for current or previous day

### testevent

* **Description**: Tests an event without triggering it
* **Arguments**: `<Event ID> <Character ID>`

### testrtti

* **Description**: Tests performance for RTTI
* **Arguments**: `<test case>`

### testtool

* **Description**: Testing tool.

### theatersrebuild

* **Description**: Rebuilds all theatres in the world. All orders will be cleaned.
* **Aliases**: trebuild

### threat

* **Description**: Adds or show threat level of player
* **Aliases**: tension
* **Arguments**: `threat amount`

### time

* **Description**: What time is it?

### timer

* **Description**: Prints out debug timing info

### timer_dump

* **Description**: Dumps debug timing info

### timer_reset

* **Description**: Resets debug timing

### timer_restart

* **Description**: Restarts (resets and starts) debug timing

### timer_start

* **Description**: Starts debug timing

### timer_stop

* **Description**: Stops debug timing

### toggle_hidden_techs

* **Description**: "Toggle show/hide all hidden techs."
* **Aliases**: tht
* **Arguments**: ``

### toggle_offset_ai_daily_update

* **Description**: Whether a country's ai daily update should be spread over a day

### toggle_silhouette_portraits

* **Description**: Enables and disables silhouette portraits.

### track_unit_controller_weights

* **Description**: Will start tracking unit controller weights for current country, should be used together with debug_unit_controller_weights to view the data.
* **Aliases**: track_ucw

### traderoutes

* **Description**: Toggle visibility of trade routes

### trigger

* **Description**: Runs a scripted trigger on selected scope
* **Aliases**: t
* **Arguments**: `<tag> scripted_trigger_name`

### trigger_ability

* **Description**: triggers an ability
* **Arguments**: `<ability_name>`

### trigger_docs

* **Description**: Print docs for triggers, effects and variables
* **Aliases**: effect_docs, scripting_docs, docs

### unit_address

* **Description**: Get the address of the first selected unit, for debugging

### unit_stats

* **Description**: lists stats of selected units

### update_loc

* **Description**: Updates the localization tag file
* **Arguments**: `localization tag`

### updateequipments

* **Description**: Updates the equipment database

### updatesubunits

* **Description**: Updates the subunit database

### version

* **Description**: Show current game version

### war_relations

* **Description**: Prints war relations info
* **Arguments**: `<tag>`

### weather

* **Description**: Toggle weather simulation

### whitepeace

* **Description**: White peace with the specified countries.
* **Aliases**: wp
* **Arguments**: `<country tags>`

### window

* **Description**: Opens or closes the specified window
* **Aliases**: wnd
* **Arguments**: `Arguments: open/close window gui name`

### xp

* **Description**: Gives Army, navy and air experience to player
* **Arguments**: `XP amount`

## Tweakables

### Agency.AutoComplete

* **Type**: bool

### Agency.InstantSlotUnlock

* **Type**: bool

### Agency.KeepExcessOperatives

* **Type**: bool

### Audio.Compressor

* **Type**: bool

### Audio.Debug

* **Type**: bool

### Audio.Debug.ExtendedRange

* **Type**: bool

### BattleSound.Debug

* **Type**: bool

### BattleSound.PlayBackground

* **Type**: bool

### BorderLOD.Threaded

* **Type**: bool

### CounterIntelligence.TestShieldColors

* **Type**: bool

### Debug.DeleteUnitEachTick

* **Type**: bool

### Debug.OldCombat

* **Type**: bool

### Decision.FastRemove

* **Type**: bool

### Decision.NoChecks

* **Type**: bool

### Draw.Borders

* **Type**: bool

### Draw.Objects

* **Type**: bool

### Draw.Postfx

* **Type**: bool

### Draw.Refractions

* **Type**: bool

### Draw.Rivers

* **Type**: bool

### Draw.ShadowBlur

* **Type**: bool

### Draw.Shadows

* **Type**: bool

### Draw.Terrain

* **Type**: bool

### Draw.Transparent

* **Type**: bool

### Draw.Tree

* **Type**: bool

### Draw.Water

* **Type**: bool

### Focus.AutoComplete

* **Type**: bool

### Focus.IgnorePrerequisites

* **Type**: bool

### Focus.NoChecks

* **Type**: bool

### IntelNetwork.Instant

* **Type**: bool

### Operation.Instant

* **Type**: bool

### PostEffectVolumes.Draw

* **Type**: bool

### PostEffectVolumes.Enabled

* **Type**: bool

### ShowBorderTypes

* **Type**: bool

### ShowTechBonus

* **Type**: bool

### Terrain.MipLevels

* **Type**: bool

### Tree.MipLevels

* **Type**: bool

### Update.Animations

* **Type**: bool

### Update.Particles

* **Type**: bool

### fa

* **Type**: bool

### resistance_system

* **Type**: bool

### supply_debug.show_debug_lines_rail

* **Type**: bool

### supply_debug.show_debug_lines_supply

* **Type**: bool

### supply_debug.show_debug_lines_train

* **Type**: bool

### supply_debug.show_debug_rivers

* **Type**: bool

