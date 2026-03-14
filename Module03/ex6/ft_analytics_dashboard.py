if __name__ == "__main__":
    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": [
                    'first_blood',
                    'level_master',
                    'treasure_seeker',
                    'boss_slayer',
                    'combo_king'
                ],
            "region": "east",
            "active": True
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": [
                    'first_blood',
                    'speed_runner',
                    'explorer'
                ],
            "region": "north",
            "active": True
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": [
                    'first_blood',
                    'level_master',
                    'treasure_seeker',
                    'pixel_perfect',
                    'combo_king',
                    'first_kill',
                    'level_10'
                ],
            "region": "central",
            "active": True
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": [
                    'first_blood',
                    'treasure_seeker',
                    'pixel_perfect',
                    'level_master',
                    'speed_runner'
                ],
            "region": "north",
            "active": False
        },
        {
            "name": "eve",
            "score": 1500,
            "achievements": [
                    'first_blood',
                    'treasure_seeker',
                    'pixel_perfect'
                ],
            "region": "south",
            "active": False
        },
        {
            "name": "frank",
            "score": 900,
            "achievements": [
                    'first_blood',
                    'explorer'
                ],
            "region": "central",
            "active": False
        },
    ]

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    high_scores = [
        player["name"]
        for player in players
        if player["score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scores}")

    scores_doubled = [
        player["score"] * 2
        for player in players
    ]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [
        player["name"]
        for player in players
        if player["active"]
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {
        player["name"]: player["score"]
        for player in players
        if player["active"]
    }
    print(f"Player scores: {player_scores}")

    high = len({
        player["name"]: player["score"]
        for player in players
        if player["score"] > 2000
    })
    medium = len({
        player["name"]: player["score"]
        for player in players
        if 1000 < player["score"] <= 2000
    })
    low = len({
        player["name"]: player["score"]
        for player in players
        if player["score"] < 1000
    })
    score_categories = {
        'high': high,
        'medium': medium,
        'low': low
    }

    print(f"Score categories: {score_categories}")

    achievements_per_player = {
        player['name']: len(player['achievements'])
        for player in players
        if player['active']
    }
    print(f"Achievement counts: {achievements_per_player}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {
        player['name']
        for player in players
    }
    print(f"Unique players: {unique_players}")

    all_achievements = {
        achievement
        for player in players
        for achievement in player["achievements"]
    }
    unique_achievements = {
        achievement
        for achievement in all_achievements
        if sum(
            achievement in player["achievements"]
            for player in players
        ) == 1
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {
        player['region']
        for player in players
        if player['active']
    }
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(all_achievements)}")

    average_score = sum(
        player["score"]
        for player in players
    ) / len(players)
    print(f"Average score: {average_score:.1f}")

    highest_score = max([
        player['score']
        for player in players
    ])
    top_performer = [
        (player['name'], player['score'], len(player['achievements']))
        for player in players
        if player['score'] == highest_score
    ]
    print(
        f"Top performer: {top_performer[0][0]} "
        f"({top_performer[0][1]} points, "
        f"{top_performer[0][2]} achievements)"
    )
