class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups anagrams from the given list of strings.

        :param strs: List of input strings
        :type strs: List[str]
        :return: List of grouped anagrams
        :rtype: List[List[str]]
        """
        # Create an empty dictionary to store anagrams
        anagram_dict = {}

        # Iterate through each string in the input list
        for s in strs:
            # Sort the characters in the string and convert it to a tuple to serve as a key
            key = tuple(sorted(s))
            # Check if the key (sorted characters) exists in the dictionary
            if key not in anagram_dict:
                # If not, create a new list with the current string as its first element
                anagram_dict[key] = [s]
            else:
                # If the key already exists, append the current string to the existing list of anagrams
                anagram_dict[key].append(s)
        # Return a list containing the values (groups of anagrams) from the dictionary
        return list(anagram_dict.values())
