## MVP

Start a timed study session, choose a building type, and review cards. If I finish, that building is placed automatically on a free square of my isometric city. For every batch of cards I review (the batch size is a setting, like 5, 10, or 50), I earn a bonus building of the same type. If I turn on deep focus mode and switch to a listed distraction (like Discord or YouTube), the session fails and I get a single broken building, with no bonus buildings. The city saves between restarts. For the MVP, buildings are placeholder shapes drawn in code, and the settings (distraction list and batch size) use Anki's default config editor, opened from Tools > Add-ons > Config.

## Phases

### Phase 1: Foundations
- [ ] Step 1: Hello world add-on (menu item in Anki)
- [ ] Step 2: Session timer (start button, countdown, building picker, deep focus toggle)

### Phase 2: Core loop
- [ ] Step 3: Card counting and bonus buildings (count cards reviewed during a session, work out how many bonus buildings that earns from the batch size)
- [ ] Step 4: Save data (store the city, including building type, working or broken, and cards reviewed, in a file outside the add-on folder)

### Phase 3: The city
- [ ] Step 5: Isometric city (grid, a few placeholder building types, working and broken versions, automatic placement)

### Phase 4: Distraction detection (MVP complete)
- [ ] Step 6: Detect the front window (Windows)
- [ ] Step 7: Fail rule (with deep focus on, a listed distraction fails the session and places a broken building)

### Phase 5: Polish and release
- [ ] Step 8: Custom settings window (batch size, distraction list, deep focus default) that opens from the Config button, plus config.md explaining each setting
- [ ] Step 9: Real building art, README screenshot or GIF, `.ankiaddon` file, AnkiWeb upload, review doc

## How I'm using AI

- Build the project plan.
- Come up with feature ideas
- Build claude.md file 

For every step:
1. AI Explains the concept before any code is written.
2. I write and/or copy the code in small pieces and ask questions about anything I don't understand.
3. I explain it back in my own words and reflect before moving on.
4. I write all my rough notes in `learningLog.md` 
5. Code comments explain the why, in my own words. The goal is that I can explain every file in this project without notes.

## Ideas after the MVP

- Week, month, and year views of the city
- Download a PNG picture of the city 