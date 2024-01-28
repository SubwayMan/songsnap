import json

# Define a function to convert data to JSONL format
def convert_to_jsonl(input_data, song_count):
    messages = [
        {"role": "system", "content": f"Generate {song_count} songs with the songwriter names split by newlines to capture the essence of the image description provided."},
        {"role": "user", "content": input_data[0]},
        {"role": "assistant", "content": input_data[1]}
    ]
    return {"messages": messages}

# description & songs
data = [
        [
"""This black and white image features a group of well-dressed individuals, likely from the mid-20th century, given the style of their clothing, which includes hats and tailored suits for men and dresses with hats for women. These fashion choices, combined with the black and white nature of the photograph, suggest a time period from the 1940s or 1950s.\n\nThe setting is unmistakably Parisian, as the Eiffel Tower looms in the background, which identifies the culture as French. The architecture of the iconic tower and its unmistakable silhouette immediately anchor the location.\n\nThe mood of the photo appears to be one of casual observation or tourism, with the individuals seemingly engaged in light conversation or observation. They do not appear to be posing for the photo but are rather captured in a candid moment. The atmosphere seems calm and perhaps a bit reflective, consistent with a foggy or overcast day in Paris, given the muted skyline.""",
"""La Vie En Rose by Edith Piaf
Autumn Leaves by Nat King Cole
Under Paris Skies by Andy Williams
April in Paris by Ella Fitzgerald & Louis Armstrong
C'est Si Bon by Eartha Kitt
Beyond the Sea by Bobby Darin
I Love Paris by Frank Sinatra
Non, Je Ne Regrette Rien by Edith Piaf
Moonlight in Vermont by Jo Stafford
Que Sera, Sera (Whatever Will Be, Will Be) by Doris Day"""
        ],
        [
"""This vibrant image captures a lively street scene in Rio de Janeiro during Carnival season. Colorful floats adorned with elaborate decorations and dancers in extravagant costumes fill the streets, creating a festive atmosphere. The energy is palpable as crowds of people dance to the rhythmic beats of samba music, with smiles and laughter abound. The iconic Christ the Redeemer statue overlooks the scene, serving as a symbol of the city's rich culture and heritage.""",
"""Mas Que Nada by Sergio Mendes & Brasil '66
The Girl from Ipanema by Stan Getz & Astrud Gilberto
Samba Pa Ti by Santana
Aquarela do Brasil by Gal Costa
Brazil by Django Reinhardt
Tico Tico by Carmen Miranda
Corcovado by Antonio Carlos Jobim
Desafinado by Joao Gilberto"""
        ],
        [
"""This electrifying image captures the raw energy of a Metallica concert in full swing. The stage is ablaze with lights and pyrotechnics as the band members thrash about, delivering powerful performances that resonate with the roaring crowd. Fans clad in Metallica merchandise and denim jackets adorned with patches form a sea of headbangers, their fists pumping in the air in unison with the music. The atmosphere is charged with adrenaline and excitement, epitomizing the intense experience of a live Metallica show.""",
"""Master of Puppets by Metallica
Enter Sandman by Metallica
One by Metallica
Fade to Black by Metallica
Nothing Else Matters by Metallica
For Whom the Bell Tolls by Metallica"""
        ],
        [
"""This retro-futuristic image transports you to a neon-drenched cityscape straight out of the 1980s. Palm trees sway against a backdrop of skyscrapers adorned with vibrant neon lights, casting a surreal glow over the bustling streets below. Sports cars with sleek, aerodynamic designs zip past, their headlights illuminating the night as they cruise to the pulsating rhythm of synthwave music. The air is thick with nostalgia, evoking memories of an era defined by arcade games, VHS tapes, and cyberpunk aesthetics.""",
"""Midnight City by M83
Miami Nights by Trevor Something
The Night by FM-84
Electric Youth by Debbie Gibson
Sunset by The Midnight
Drive by The Cars
Nightcall by Kavinsky
Far Cry by Mitch Murder
Starman by Carpenter Brut"""
        ],
        [
"""This vibrant image captures the essence of a bustling pop concert in a packed stadium. Colorful lights flash and illuminate the stage as the pop star, adorned in glittering attire, commands the attention of thousands of adoring fans. The crowd erupts in cheers and applause, their excitement palpable as they sing along to every hit song. Giant screens project larger-than-life images of the performer, creating an immersive experience for concertgoers. It's a celebration of music and unity, where people from all walks of life come together to dance, sing, and experience the magic of pop music.""",
"""Shape of You by Ed Sheeran
Uptown Funk by Mark Ronson ft. Bruno Mars
Dynamite by BTS
Roar by Katy Perry
Can't Stop the Feeling! by Justin Timberlake
Firework by Katy Perry
Happy by Pharrell Williams
Love Me Like You Do by Ellie Goulding
Closer by The Chainsmokers ft. Halsey
Shake It Off by Taylor Swift
"""
        ],
        [
"""This image encapsulates the lively ambiance of the 1980s pop scene, characterized by its vivid colors, flamboyant fashion, and high-energy atmosphere. Neon lights flood the dance floor of a bustling nightclub, where crowds sway to the pulsating beats of synth-driven pop music. With their leg warmers, shoulder pads, and teased hair, dancers showcase iconic moves like the moonwalk and the cabbage patch. It's a decade marked by extravagance and enthusiasm, where pop culture reigned supreme and music became the heartbeat of a generation.""",
"""Billie Jean by Michael Jackson
Wake Me Up Before You Go-Go by Wham!
Take On Me by a-ha
Girls Just Want to Have Fun by Cyndi Lauper
Don't Stop Believin' by Journey
Every Breath You Take by The Police
Sweet Child o' Mine by Guns N' Roses
Material Girl by Madonna
I Wanna Dance with Somebody (Who Loves Me) by Whitney Houston"""
        ],
        [
"""This cozy image transports you to a dimly lit bedroom on a rainy day, where the soft crackle of vinyl fills the air. A vintage record player spins soothing lo-fi beats, creating a tranquil atmosphere perfect for relaxation and introspection. Sunlight filters through the window, casting a warm glow on piles of books and scattered art prints. With a steaming cup of tea in hand, you sink into a plush armchair, enveloped in the gentle melodies of lo-fi music. It's a moment of calm amidst the chaos of everyday life, where time seems to stand still and worries melt away.""",
"""Space Cadet by Kupla
Rainy Day by Tom Doolie
Sunday Vibes by SwuM
Reflect by Idealism"""
        ],
        [
"""This timeless image captures the essence of a dimly lit jazz club on a bustling city street corner. The air is thick with the rich aroma of coffee and the sound of smooth, soulful melodies drifting from the stage. Musicians, bathed in warm spotlight, effortlessly improvise intricate solos on their instruments, their passion evident in every note. Patrons, seated at intimate tables adorned with flickering candles, sip cocktails and tap their feet to the infectious rhythm of the music. It's an atmosphere steeped in sophistication and spontaneity, where the art of jazz comes alive with each electrifying performance.""",
"""Take Five by Dave Brubeck
So What by Miles Davis
Summertime by Ella Fitzgerald & Louis Armstrong
My Favorite Things by John Coltrane
All Blues by Miles Davis
Autumn Leaves by Cannonball Adderley
Blue in Green by Miles Davis
Fly Me to the Moon by Frank Sinatra
A Night in Tunisia by Dizzy Gillespie"""
        ],
        [
"""This dynamic image captures the electrifying energy of a K-pop concert, where vibrant colors, dazzling choreography, and infectious beats collide to create an unforgettable spectacle. The stage is illuminated by a kaleidoscope of lights, as K-pop idols command the attention of thousands of fans with their mesmerizing performances. Fans, known as "K-poppers," wave light sticks in unison, chanting fan chants and singing along to every song with passion and fervor. It's a celebration of youth, pop culture, and Korean musical innovation, where the boundary between performer and audience blurs in a euphoric display of unity and excitement.""",
"""Dynamite by BTS
Kill This Love by BLACKPINK
Boy With Luv by BTS ft. Halsey
Love Scenario by iKON
Fancy by TWICE
How You Like That by BLACKPINK
DNA by BTS"""
        ],
        [
"""Step into the neon-lit world of a retro arcade, where the air is alive with the sounds of chirping electronic melodies and the clatter of buttons being mashed. Rows of vintage arcade cabinets line the walls, their screens casting a kaleidoscope of colors onto the dimly lit room. Gamers huddle around their favorite machines, their faces illuminated by the glow of pixelated graphics as they compete for high scores and bragging rights. The scent of popcorn and the faint hum of arcade machines create a nostalgic atmosphere that transports visitors back to a simpler time, where the arcade was the ultimate destination for fun and excitement.""",
"""Pac-Man Fever by Buckner & Garcia
Donkey Kong Theme by Nintendo
Space Invaders by Player One
Frogger by Konami Kukeiha Club
Galaga by Namco Sounds
Tetris Theme by Nintendo
Street Fighter II Theme by Capcom
Dig Dug by Atari
Mario Bros. Theme by Nintendo
Centipede by Atari"""
        ]
]

# Write data to the JSONL file
with open('trainingData.jsonl', 'w') as jsonl_file:
    cnt = 0
    for item in data:
        song_count = item[1].count('\n') + 1
        jsonl_entry = json.dumps(convert_to_jsonl(item, song_count))
        jsonl_file.write(jsonl_entry + '\n')
        cnt += 1
        print(cnt, 'data point created...')

print('Done!')
