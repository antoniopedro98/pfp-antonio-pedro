"""
Bootstrapping handler.

This module aims to center the process 
and computation of bootstrapping.

Author: Antonio Pedro Santos Alves
Advisor: Marcos Kalinowski
"""

import random
import math
from statistics import mean, pstdev


class BootstrappingUtils:    
    def __init__(self, answers: list[any], options: list[str], replacements: int = 1000, population_size: int = 1000, confidence: float = 0.95):
        self.answers = answers
        self.options = options
        self.replacements = replacements
        self.population_size = population_size
        self.confidence = confidence


    def bootstrapping(self, question_type: str = 'single') -> dict:
        """
           Create bootstrapping for 'to-choose-options' questions,
           like both single and multiple choice.
        """
        populations = []
        for _ in range(self.replacements):
            if question_type == 'single':
                population = self.single_option_sampling()
                
            elif question_type == 'multiple':
                population = self.multiple_option_sampling()
            
            populations.append(population)
        
        # compute the percentage of answers in each option for each population/replacement
        population_metrics = {option: 
            {
                'population': [],
                'confidence': ()
            } for option in self.options
        }
        
        # add population mean total answers
        for population in populations:
            for option in population:
                population_metrics[option]['population'].append( (population[option] / self.population_size) * 100 )

        # compute confidence
        for option in population_metrics:
            population_metrics[option]['confidence'] = self.confidence_interval(population_metrics[option]['population'])

        return population_metrics


    def bootstrapping_numerical_fields(self) -> dict:
        """
            Create bootstrapping for 'set-numerical-value' questions,
            like 'What is your age?', 'What percentage...'.
        """
        population = self.numerical_field_sampling()
        confidence = self.confidence_interval(population)

        population_metric = {
            'population': population,
            'confidence': confidence
        }
        
        return population_metric
        

    def single_option_sampling(self) -> dict:
        """
            Execute a sampling of answers a 'population_size' times 
            given a previous set of real answers.

            In this case, each answer represents one single option.
        """
        # ensure that all options will be filled - with 0 at least
        population_answers = {option: 0 for option in self.options}
        
        for _ in range(self.population_size):
            rand_idx = random.randrange(len(self.answers))
            random_option = self.answers[rand_idx]
            population_answers[random_option] += 1
            
        return population_answers


    def multiple_option_sampling(self) -> dict:
        """
            Execute a sampling of answers a 'population_size' times 
            given a previous set of real answers.

            In this case, each answer represents a subset of
            valid options, once we are dealing with multiple 
            option question
        """
        # ensure that all options will be filled - with 0 at least
        population_answers = {option: 0 for option in self.options}
        
        for _ in range(self.population_size):
            rand_idx = random.randrange(len(self.answers))
            random_option_list = self.answers[rand_idx]
            # increase option total of answers for each one assigned
            for random_option in random_option_list:
                population_answers[random_option] += 1
        
        return population_answers


    def numerical_field_sampling(self) -> list:
        """
            Execute a sampling of answers a 'population_size' times
            given a previous set of answered value.

            In this case, each answer was a numerical value set.
            We choose one that already exists.
        """
        population_answers = []
        
        for _ in range(self.population_size):
            # only choose one value inside of what people have chosen
            rand_idx = random.randrange(len(self.answers))
            random_option = self.answers[rand_idx]
            population_answers.append(random_option)
            
        return population_answers


    def confidence_interval(self, data_points: list) -> tuple:
        """
            Compute the confidence interval for the population answers.

            Based on https://www.indeed.com/career-advice/career-development/how-to-calculate-confidence-interval
        """
        # mean
        X = mean(data_points)
        # population standard deviation
        S = pstdev(data_points)
        # data points length
        n = len(data_points)
        # square root data_points length
        sr_n = math.sqrt(n)
        # standard error
        standard_error = S / n
        # margin error
        margin_error = standard_error * 2
        
        lower_value = X - (self.confidence * (S / sr_n))
        upper_value = X + (self.confidence * (S / sr_n))
        
        return (lower_value, X, upper_value)
