def user_test():
    
    # Import libraries
    import pandas as pd
    import joblib
    
    # Load trained model
    prediction = joblib.load('prediction.pkl')
    
    analysis = joblib.load('analysis.pkl')
    
    # Define features required for analysis
    pre_match = ['second_serves_return_points_won_%', 'break_point_convert_%']
    
    match_analysis = ['first_serves_points_won_%', 'second_serves_points_won_%', 'break_point_save_%',
                      'first_serves_return_points_won_%', 'break_point_convert_%', 'break_points_return_total']
    
    # Model Selection Menu
    print("Please select model:")
    print("Prediction: please enter '1'")
    print("Analysis: please enter '2'")
    
    model_selection = input('Please state your choice: ')
    
    if model_selection == '1':
        
        # Prediction Model Selection Menu
        print("")
        print("For predictions based on")
        print("1 player: please enter '1'")
        print("2 player: please enter '2'")

        number_of_players = input('Please state your choice: ')


        # Function to predict chance of a player winning a match based on 2 features
        if number_of_players == '1':

            # Request user to input features
            user_feature_1 = input('What is the second serve return points won % ? ')
            user_feature_2 = input('What is the break point conversion rate ? ')


            df_prediction_testing = pd.DataFrame(columns = pre_match)
            df_prediction_testing['second_serves_return_points_won_%'] = [float(user_feature_1)]
            df_prediction_testing['break_point_convert_%'] = [float(user_feature_2)]

            user_test_prediction = prediction.predict_proba(df_prediction_testing)

            print("")
            print(f"The likelihood of the player winning is: {round(user_test_prediction[0][1] * 100, 2)} %")


        # Function to predict relative chance of a player winning a match based on 2 features from both players
        elif number_of_players == '2':

            # Request user to input features
            player1_feature_1 = input('For player 1: What is the second serve return points won % ? ')
            player1_feature_2 = input('For player 1: What is the break point conversion rate ? ')

            player2_feature_1 = input('For player 2: What is the second serve return points won % ? ')
            player2_feature_2 = input('For player 2: What is the break point conversion rate ? ')


            df_player1 = pd.DataFrame(columns = pre_match)
            df_player1['second_serves_return_points_won_%'] = [float(player1_feature_1)]
            df_player1['break_point_convert_%'] = [float(player1_feature_2)]

            df_player2 = pd.DataFrame(columns = pre_match)
            df_player2['second_serves_return_points_won_%'] = [float(player2_feature_1)]
            df_player2['break_point_convert_%'] = [float(player2_feature_2)]

            player1_prediction = prediction.predict_proba(df_player1)
            player2_prediction = prediction.predict_proba(df_player2)

            player1_chance = player1_prediction[0][1] / (player1_prediction[0][1] + player2_prediction[0][1])
            player2_chance = player2_prediction[0][1] / (player1_prediction[0][1] + player2_prediction[0][1])


            print("")
            print(f"The likelihood of the player 1 winning is: {round(player1_chance * 100, 2)} %")
            print("")
            print(f"The likelihood of the player 2 winning is: {round(player2_chance * 100, 2)} %")
    
    
    # Function to analyze completed matches to view player performance during the match
    # This function can be used on individual set statistics to measure momentum gain/loss during the match
    
    elif model_selection == '2':
        
        # Request user to input features
        user_feature_1 = input('What is the first serves points won % ? ')
        user_feature_2 = input('What is the second serves points won % ? ')
        user_feature_3 = input('What is the break point save % ? ')
        user_feature_4 = input('What is the first serve return points won % ? ')
        user_feature_5 = input('What is the break point conversion rate ? ')
        user_feature_6 = input('What is the total number of break point chances ? ')


        df_analysis_testing = pd.DataFrame(columns = match_analysis)
        df_analysis_testing['first_serves_points_won_%'] = [float(user_feature_1)]
        df_analysis_testing['second_serves_points_won_%'] = [float(user_feature_2)]
        df_analysis_testing['break_point_save_%'] = [float(user_feature_3)]
        df_analysis_testing['first_serves_return_points_won_%'] = [float(user_feature_4)]
        df_analysis_testing['break_point_convert_%'] = [float(user_feature_5)]
        df_analysis_testing['break_points_return_total'] = [float(user_feature_6)]

        user_test_analysis_result = analysis.predict(df_analysis_testing)

        user_test_analysis_proba = analysis.predict_proba(df_analysis_testing)

        if user_test_analysis_result[0] == 0:
            print("")
            print(f"This player most likely lost the match and he had a {round(user_test_analysis_proba[0][1] * 100, 2)} % chance of winning the match.")
        elif user_test_analysis_result[0] == 1:
            print("")
            print(f"This player most likely won the match and he had a {round(user_test_analysis_proba[0][1] * 100, 2)} % chance of winning the match.")