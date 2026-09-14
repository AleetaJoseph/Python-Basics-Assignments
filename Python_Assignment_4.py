feedback_data = {
 'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
 'Feedback': [
 ' Very GOOD Service!!!',
 'poor support, not happy ',
 'GREAT experience! will come again.',
 'okay okay...',
 ' not BAD',
 'Excellent care, excellent staff!',
 'good food and good ambience!',
 'Poor response and poor handling of issue',
 'Satisfied. But could be better.',
 'Good support... quick service.'
 ],
 'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}




#Step 2: Add More Feedbacks

#● Ask the user to enter how many more feedbacks they want to add.
#● For each feedback, collect the following inputs from the user:
# Name
# Written Feedback (text)
# Rating (1–5)
#● Automatically increment S_No starting from 11 onward.
#● Append all new data into the feedback_data dictionary.

# number = int(input("How many more feedbacks do you want to add? "))

# for i in range(number):

#     name = input("Enter Name: ")
#     feedback = input("Enter Feedback: ")
#     rating = int(input("Enter Rating (1-5): "))


#     s_no = len(feedback_data['S_No']) + 1


#     feedback_data['S_No'].append(s_no)
#     feedback_data['Name'].append(name)
#     feedback_data['Feedback'].append(feedback)
#     feedback_data['Rating'].append(rating)

#     print(feedback_data)


    # Step 3: Text Cleaning

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    
    feedback = feedback.replace('.', '')
    feedback = feedback.replace(',', '')
    feedback = feedback.replace('!', '')
    feedback = feedback.replace('?', '')

    
    feedback = ' '.join(feedback.split())

  
    feedback = feedback.lower()

    feedback_data['Feedback'][i] = feedback


print(feedback_data['Feedback'])



#Step 4: Word Count Insights (4 marks)
# Create a function count_word_in_feedbacks(word) that:
# ● Takes a word as input.
# ● Returns how many feedbacks contain that word (case-insensitive match).
# Use this function to print:
# ● Number of feedbacks containing "good"
# ● Number of feedbacks containing "poor"
# ● Number of feedbacks containing "excellent"


def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        if word.lower() in feedback:
            count += 1

    return count


print("Number of feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Number of feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Number of feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))




# Step 5: Final Summary & Insights

# Display the final cleaned feedback_data (dictionary of lists).

print(feedback_data)


# Print the average rating from all feedbacks.
total_rating = sum(feedback_data['Rating'])
number_of_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / number_of_feedbacks

print("Average Rating:", average_rating)


# 3. Find and display the feedback with the longest comment (in terms of word count)
longest_feedback = ""
longest_word_count = 0

for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())

    if word_count > longest_word_count:
        longest_word_count = word_count
        longest_feedback = feedback

print(longest_feedback)
print("Word Count:", longest_word_count)


# Print the list of unique words used across all feedbacks (avoid duplicates).
unique_words = set()

for feedback in feedback_data['Feedback']:
    words = feedback.split()

    for word in words:
        unique_words.add(word)


print(unique_words)