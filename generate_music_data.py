import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create 520 unique songs
song_names = [
    'Blinding Lights', 'Levitating', 'Heat Waves', 'As It Was', 'Anti-Hero',
    'Cruel Summer', 'Unholy', 'Kill Bill', 'Flowers', 'Vampire',
    'Blank Space', 'Shape of You', 'Shut Up and Dance', 'Take Me Out', 'Mr. Brightside',
    'Come Together', 'Bohemian Rhapsody', 'Imagine', 'Hotel California', 'Stairway to Heaven',
    'Starboy', 'Bad Guy', 'Without You', 'Peaches', 'Save Your Tears',
    'Kiss Me More', 'Industry Baby', 'Need to Know', 'Drivers License', 'Good 4 U',
    'Jealousy Jealousy', 'Deja Vu', 'Traitor', 'All the Stars', 'Happier Than Ever',
    'Butter', 'Dynamite', 'Permission to Dance', 'Yet to Come', 'Jungkook Standing',
    'Ariana Thank U Next', 'Ariana Into You', 'Ariana God is a Woman', 'Ariana Dangerous Woman', 'Ariana Breathin',
    'Drake One Dance', 'Drake Gods Plan', 'Drake In My Feelings', 'Drake Toosie Slide', 'Drake Marvins Room',
    'Rihanna Umbrella', 'Rihanna Work', 'Rihanna We Found Love', 'Usher Yeah', 'Usher U Remind Me',
    'Bruno Mars Just the Way', 'Bruno Mars Uptown Special', 'Bruno Mars When I Was Your Man', 'Bruno Mars 24K Magic', 'The Weeknd Party Monster',
    'Post Malone Circles', 'Post Malone Psycho', 'Post Malone Congratulations', 'Post Malone White Iverson', 'Dua Lipa New Rules',
    'Dua Lipa IDGAF', 'Dua Lipa Physical', 'Dua Lipa Break My Heart', 'Billie Eilish Ocean Eyes', 'Billie Eilish When We All Fall Asleep',
    'Lose Yourself', 'Without Me', 'The Real Slim Shady', 'Stan', 'Love the Way You Lie',
    'Rap God', 'Godzilla', 'Till I Collapse', 'Mockingbird', 'Sing for the Moment',
    'Not Afraid', 'Recovery', 'Beautiful', 'Cleanin Out My Closet', 'Stronger Than I Was',
    'In Da Club', 'Candy Shop', 'Many Men', 'PImp', 'I Got Rich',
    'Lil Wayne Tha Block is Hot', 'Lil Wayne A Milli', 'Lil Wayne Hot Boyz', 'Lil Wayne Got Money', 'Jay-Z Izzo',
    'Jay-Z 99 Problems', 'Jay-Z Dirt Off Your Shoulder', 'Jay-Z Girls Girls Girls', 'Jay-Z Can I Get A', 'Nas If I Ruled the World',
    'Nas The World Is Yours', 'Nas Illmatic', 'Nas New York State of Mind', 'Biggie Juicy', 'Biggie Mo Money Mo Problems',
    'Biggie Ready Die', 'Tupac California Love', 'Tupac Changes', 'Tupac All Eyez on Me', 'Tupac Brendas Got a Baby',
    'Kendrick Lamar Swimming Pools', 'Kendrick Lamar Humble', 'Kendrick Lamar Alright', 'Kendrick DNA', 'Kendrick Backseat Freestyle',
    'J Cole Power Trip', 'J Cole No Role Modelz', 'J Cole Middle Child', 'J Cole Crooked Smile', 'Drake Hotline Bling',
    'Drake Started from Bottom', 'Drake Marvin Room', 'Drake 0 to 100', 'Migos Bad and Boujee', 'Gunna Drip Season',
    'Lil Baby Drip Too Hard', 'Lil Durk Viral', 'Playboi Carti Die For U', 'Travis Scott Sicko Mode', 'ASAP Rocky Long Live',
    'Tyler Creator', 'Tyler Creator Yonkers', 'Frank Ocean Thinkin Bout You', 'Frank Ocean Pink Maibi', 'Donald Glover Awaken My Love',
    'Wonderwall', 'Champagne Supernova', 'Wonderfully Young', 'Dont Look Back in Anger', 'Rock and Roll',
    'Whole Lotta Love', 'Black Dog', 'Immigrant Song', 'Kashmir', 'Since Ive Been Loving You',
    'Going to California', 'Dyer Maker', 'The Ocean', 'Ramble On', 'Thank You',
    'Four Sticks', 'Hey Jude', 'Let It Be', 'Yesterday', 'Something',
    'In My Life', 'A Day in the Life', 'She Loves You', 'I Want to Hold Your Hand', 'Twist and Shout',
    'Norwegian Wood', 'Strawberry Fields Forever', 'Penny Lane', 'Dear Prudence', 'While My Guitar Gently Weeps',
    'Another One', 'We Will Rock', 'Stone Cold Crazy', 'Tie Your Mother', 'I Want It All',
    'Play Game', 'Time', 'Wish You Were Here', 'Money', 'Run Like Hell',
    'Brain Damage', 'Comfortably Numb', 'In the Flesh', 'Young Lust', 'Sympathy',
    'Brown Sugar', 'Satisfaction', 'Jumpin Jack Flash', 'Street Fighting', 'Angie',
    'My Generation', 'Wont Get Fooled', 'Baba ORiley', 'Pinball Wizard', 'Light My Fire',
    'Break On Through', 'LA Woman', 'Riders Rain', 'Purple Haze', 'Foxy Lady',
    'Star Spangled Banner', 'Manic Depression', 'Heroes', 'Starman', 'Space Oddity',
    'Changes', 'One Kiss', 'Your Name', 'Animals', 'Titanium',
    'Clarity', 'Scary Monsters', 'Wake Me Up', 'Hey Brother', 'The Nights',
    'Levels', 'Dont You Worry Child', 'Eating', 'Greyhound', 'Animals Remix',
    'Pride in the Name Love', 'Skin', 'Satisfaction Benny Benassi', 'Sandstorm', 'Cafe Del Mar',
    'Strobe', 'For An Angel', 'Armin Around the World', 'Communication', 'In Search of Sunrise',
    'Beautiful Life', 'Invincible', 'Together', 'Waiting for Love', 'Lay Me Down',
    'More Than You Know', 'Sun is Shining', 'Where Are You Now', 'Lean On', 'Be',
    'Steal the Show', 'Waiting for You', 'Loneliness', 'Turning Tables', 'Island Girl',
    'Like Home', 'Lonely Heart', 'Love Again', 'Empty Streets', 'Never Stop',
    'Digital Love', 'One More Time', 'Get Lucky', 'Instant Crush', 'Touch',
    'Fragment of Time', 'Lounge Act', 'Something About Us', 'All is Full Love', 'Electric Feel',
    'Smooth Criminal', 'Billie Jean', 'Beat It', 'Human Nature', 'Black or White',
    'They Dont Care About Us', 'Dirty Diana', 'Bad', 'Thriller', 'You Are Not Alone',
    'Earth Song', 'Rock My World', 'Who Is It', 'Remember the Time', 'Gone Too Soon',
    'Careless Whisper', 'Wake Me Up George', 'Fastlove', 'Outside', 'Father Figure',
    'As George', 'Faith', 'Hard Day', 'Older', 'Spinning the Wheel',
    'Twilight Hour', 'Female Lover', 'Sex is on My Mind', 'Baby Let Me Love', 'Mariah Carey Vision',
    'Vision of Love', 'We Belong Together', 'I Dont Want a Hero', 'Hero', 'Emotions',
    'Someday', 'Forever My Love', 'Love Takes Time', 'Thank God I Found', 'I Still Believe',
    'Music Box', 'Greatest Hits Medley', 'My Love Take You', 'Forever', 'Never Too Far Apart',
    'Alicia Keys Fallingslowly', 'Fallin', 'Woman Like Me', 'I Keep On', 'You Dont Know My Name',
    'If I Aint Have You', 'Try Sleeping', 'Teenage Love', 'Give Me You', 'Diary',
    'A Woman Worth', 'When You Really Love', 'Undercover', 'Another Way', 'Substitute You',
    'Go Again', 'Forever Together', 'Close Your Eyes', 'Never Let', 'I Will Always Love You',
    'Greatest Love All Time', 'I Have Nothing', 'All at Once', 'One Moment in Time', 'Who Do You Love',
    'Queen of the Night', 'My Love is', 'Didnt Know', 'Gasolina', 'Dile al Amor',
    'Bachata Rosa', 'Livin La Vida Loca', 'Tequila', 'La Bamba', 'El Manisero',
    'Mas Que Nada', 'Girl from Ipanema', 'Mambo No 5', 'A Little Less Conversation', 'Spanish Eyes',
    'Smooth', 'Maria Maria', 'One Love', 'Buffalo Soldier', 'Jamming',
    'Redemption Song', 'Get Up Stand Up', 'Iron Lion Zion', 'Three Little Birds', 'Could You Be Loved',
    'No Woman No Cry', 'Is This Love', 'Concrete Jungle', 'Stir It Up', 'Exodus',
    'Waiting in Vain', 'Burnin Down House', 'Lively Up Yourself', 'Rainbow Country', 'One Barrel',
    'Easy Skanking', 'Natural Mystic', 'Keep On Moving', 'Survival', 'Ambush Attack',
    'Trench Town Rock', 'So Many Times', 'Stand Alone', 'African Heritage', 'All Day All Night',
    'Such Great Heights', 'Nothing Between Us', 'New Slang', 'Holland 1945', 'Electric Feel Part',
    'Kids Will Be Skeletons', 'Float On', 'Uptight', 'All These Things Part', 'This Must Be Place',
    'Burning Down the House', 'Once in Lifetime', 'Psycho Killer', 'Road to Nowhere', 'Crosseyed',
    'Torn', 'Smooth Like Butter', 'The Middle', 'Steal My Sunshine', 'Semi Charmed Life',
    'More Than This', 'Wonderwall Oasis', 'Dont Look Back', 'Live Forever', 'Champagne Super',
    'Sweet Dreams', 'Enjoy the Silence', 'Personal Jesus', 'Never Let Me Down', 'Policy Control',
    'Shake It Out', 'Only If For Night', 'Florence Cosmic Love', 'You Have Loved Me', 'Spectrum',
    'Blinding Me With Flowers', 'Take Me Home Country', 'Home Country Home', 'Coming Home', 'Sweet Escape',
    'Tonight Tonight', 'Disarm', 'Today Smashing', 'Bullet with Name', 'Suffer',
    'Luna', 'Starla', 'Zero', 'Rhinoceros', 'Geek USA',
    'When the Stars Shine', 'Tonight Tonights Night', 'The Beginning', 'Drunk on You', 'Last Nite',
    'Reptilia', 'Undercover Martyn', 'Seven Nation', 'Red Right Hand', 'Matinee',
    'Dark Was Night', 'Do Not Disturb', 'Fluorescent', 'All Cats Black', 'Sex on Fire',
    'Dusty Womans Day', 'Kings of Leon', 'Southern Star', 'Holy Roller', 'Knocked up',
    'What R They Growing', 'Wasted Time', 'Black Bones', 'Nathan for You', 'Splitter',
    'Calender', 'Country Roads', 'Life is a Highway', 'Folsom Prison Blues', 'I Walk the Line',
    'Ring of Fire', 'Jackson', 'Dolly Parton Jolene', 'Coal Miner Daughter', 'White Lightning',
    'Will the Circle Unbroken', 'On the Road Again', 'Always On My Mind', 'Crazy', 'Stand by Your Man',
    'Your Cheatin Heart', 'Mammas Dont Lettings', 'Willie Nelson', 'Good Hearted Woman', 'Waylon Jennings Outlaw',
    'Mommas Taught Me', 'Wanted Outlaws', 'Me and Bobby', 'Help Me Make Through Night', 'Golden Earring Radar Love',
    'Take It Easy', 'Brown Eyed Girl', 'Ghost Riders', 'There Goes My Everything', 'Country Sunshine',
    'Small Town Saturday', 'Back Where', 'Find Out Whose Loving', 'Long as Theres Love', 'Tennessee Flat Top',
    'Hello Darling', 'Silver Threads', 'Tennessee Rain', 'Old Dogs New Tricks', 'Rocky Mountain High',
    'Sunshine on My Shoulders', 'Annies Song', 'Summertime', 'St Louis Blues', 'Basin Street Blues',
    'Moanin Low', 'Lover Come Back', 'All Blue', 'Kind of Blue', 'So What',
    'Autumn Leaves', 'In a Sentimental Mood', 'Misty', 'Georgia on My Mind', 'Unforgettable',
    'Fly Me to Moon', 'The Way You Look Tonight', 'Stardust', 'Moonglow', 'Body and Soul',
    'All of Me', 'These Foolish Things', 'Satin Doll', 'Take the A Train', 'Dont Get Around Much',
    'In the Mood', 'One OClock Jump', 'Sent for You Yesterday', 'Hoagy Carmichael', 'Lazy River'
]

# Ensure exactly 520 songs
song_names = song_names[:520]
while len(song_names) < 520:
    song_names.append(f'Song {len(song_names) + 1}')

# Create matching artists
artists = [
    'The Weeknd', 'Dua Lipa', 'Glass Animals', 'Harry Styles', 'Taylor Swift',
    'Taylor Swift', 'Sam Smith', 'SZA', 'Miley Cyrus', 'Olivia Rodrigo',
    'Taylor Swift', 'Ed Sheeran', 'Walk the Moon', 'Franz Ferdinand', 'The Killers',
    'The Beatles', 'Queen', 'John Lennon', 'Eagles', 'Led Zeppelin',
    'The Weeknd', 'Billie Eilish', 'The Kid LAROI', 'Justin Bieber', 'The Weeknd',
    'SZA', 'Lil Nas X', 'Megan Thee Stallion', 'Olivia Rodrigo', 'Olivia Rodrigo',
    'Olivia Rodrigo', 'Olivia Rodrigo', 'Olivia Rodrigo', 'Kendrick Lamar', 'Olivia Rodrigo',
    'BTS', 'BTS', 'BTS', 'BTS', 'BTS',
    'Ariana Grande', 'Ariana Grande', 'Ariana Grande', 'Ariana Grande', 'Ariana Grande',
    'Drake', 'Drake', 'Drake', 'Drake', 'Drake',
    'Rihanna', 'Rihanna', 'Rihanna', 'Usher', 'Usher',
    'Bruno Mars', 'Bruno Mars', 'Bruno Mars', 'Bruno Mars', 'The Weeknd',
    'Post Malone', 'Post Malone', 'Post Malone', 'Post Malone', 'Dua Lipa',
    'Dua Lipa', 'Dua Lipa', 'Dua Lipa', 'Billie Eilish', 'Billie Eilish',
    'Eminem', 'Eminem', 'Eminem', 'Eminem', 'Eminem',
    'Eminem', 'Eminem', 'Eminem', 'Eminem', 'Eminem',
    'Eminem', 'Eminem', 'Eminem', 'Eminem', 'Eminem',
    '50 Cent', '50 Cent', '50 Cent', '50 Cent', '50 Cent',
    'Lil Wayne', 'Lil Wayne', 'Lil Wayne', 'Lil Wayne', 'Jay-Z',
    'Jay-Z', 'Jay-Z', 'Jay-Z', 'Jay-Z', 'Nas',
    'Nas', 'Nas', 'Nas', 'Biggie', 'Biggie',
    'Biggie', '2Pac', '2Pac', '2Pac', '2Pac',
    'Kendrick Lamar', 'Kendrick Lamar', 'Kendrick Lamar', 'Kendrick Lamar', 'Kendrick Lamar',
    'J. Cole', 'J. Cole', 'J. Cole', 'J. Cole', 'Drake',
    'Drake', 'Drake', 'Drake', 'Migos', 'Gunna',
    'Lil Baby', 'Lil Durk', 'Playboi Carti', 'Travis Scott', 'A$AP Rocky',
    'Tyler The Creator', 'Tyler The Creator', 'Frank Ocean', 'Frank Ocean', 'Donald Glover',
    'Oasis', 'Oasis', 'Oasis', 'Oasis', 'Led Zeppelin',
    'Led Zeppelin', 'Led Zeppelin', 'Led Zeppelin', 'Led Zeppelin', 'Led Zeppelin',
    'Led Zeppelin', 'Led Zeppelin', 'Led Zeppelin', 'Led Zeppelin', 'Led Zeppelin',
    'Led Zeppelin', 'The Beatles', 'The Beatles', 'The Beatles', 'The Beatles',
    'The Beatles', 'The Beatles', 'The Beatles', 'The Beatles', 'The Beatles',
    'The Beatles', 'The Beatles', 'The Beatles', 'The Beatles', 'The Beatles',
    'Queen', 'Queen', 'Queen', 'Queen', 'Queen',
    'Queen', 'Pink Floyd', 'Pink Floyd', 'Pink Floyd', 'Pink Floyd',
    'Pink Floyd', 'Pink Floyd', 'Pink Floyd', 'Pink Floyd', 'The Rolling Stones',
    'The Rolling Stones', 'The Rolling Stones', 'The Rolling Stones', 'The Rolling Stones', 'The Rolling Stones',
    'Led Zeppelin', 'Led Zeppelin', 'Led Zeppelin', 'The Who', 'The Who',
    'The Who', 'The Who', 'The Doors', 'The Doors', 'The Doors',
    'The Doors', 'Jimi Hendrix', 'Jimi Hendrix', 'Jimi Hendrix', 'Jimi Hendrix',
    'David Bowie', 'David Bowie', 'David Bowie', 'David Bowie', 'Queen',
    'Queen', 'Queen', 'Dua Lipa', 'Calvin Harris', 'Martin Garrix',
    'David Guetta', 'Zedd', 'Marshmello', 'Swedish House Mafia', 'Avicii',
    'Avicii', 'Avicii', 'Avicii', 'Swedish House Mafia', 'Toto',
    'Tiësto', 'Garrix', 'Kygo', 'ATB', 'Armin van Buuren',
    'Armin van Buuren', 'ATB', 'Dash Berlin', 'Above Beyond', 'Above Beyond',
    'Avicii', 'Labrinth', 'Diplo', 'Skrillex', 'Yellow Claw',
    'Jack Ü', 'Diplo', 'Porter Robinson', 'Porter Robinson', 'Zedd',
    'Diplo', 'Daft Punk', 'Daft Punk', 'Pharrell', 'Giorgio Moroder',
    'Daft Punk', 'Pharrell', 'Daft Punk', 'Justice', 'Justice',
    'Justice', 'Justice', 'MGMT', 'Strokes', 'Strokes',
    'MGMT', 'Vampire Weekend', 'MGMT', 'Black Lips', 'MGMT',
    'MGMT', 'Grizzly Bear', 'Vampire Weekend', 'Animal Collective', 'Grizzly Bear',
    'Phoenix', 'The White Stripes', 'The White Stripes', 'The Black Lips', 'The White Stripes',
    'Portugal', 'Bloc Party', 'New Order', 'Chromatics', 'Chromatics'
] + ['Various Artists'] * 150

# Ensure exactly 520
artists = artists[:520]

# Create genres (ensure same length)
genres = ['Pop', 'Rock', 'Hip-Hop', 'R&B', 'Jazz', 'Electronic', 'Country', 'Latin', 'Soul', 'Indie'] * 52

# Create other fields with exact 520 length
music_data = {
    'song_name': song_names,
    'artist': artists,
    'genre': genres,
    'duration_sec': np.random.randint(180, 360, 520),
    'release_year': np.random.randint(1950, 2024, 520),
    'rating': np.random.uniform(3.5, 5.0, 520).round(2),
    'popularity_score': np.random.uniform(50, 100, 520).round(2),
    'mood': np.random.choice(['Happy', 'Sad', 'Energetic', 'Chill', 'Romantic', 'Melancholic', 'Upbeat'], 520),
    'language': np.random.choice(['English', 'Spanish', 'French', 'Portuguese', 'Italian', 'German', 'Japanese', 'Korean'], 520),
    'album': ['Album ' + str(i % 100 + 1) for i in range(520)],
    'streams': np.random.randint(1000000, 500000000, 520)
}

# Create DataFrame
df = pd.DataFrame(music_data)

# Save to CSV
df.to_csv('music.csv', index=False)
print(f"✅ Generated music dataset with {len(df)} songs!")
print(f"Columns: {list(df.columns)}")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head(10))
