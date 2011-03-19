#!/usr/bin/python
#-*- coding:utf-8 -*-

from data_manager import *
from classification_algorithms import *
from machine import training_machine
from global_algorithms import *

from datetime import datetime
import random

"""
Prototypes Selection Algorithms
"""

__author__ =  'Filipe Wanderley Lima (fwl), Juliana Medeiros de Lucena (jml) and Tiago Ferreira Lima (tfl2)'

def cnn(solution, data_set):
	"""
	Condensed Nearest Neighbor selection of prototypes

	@type data_set: dict
	@param data_set: The original data set

	@rtype: dcit
	@returns: The consistent subset of the original data set 
	"""
	
	data_set_filtered = dict()
	changed = True		

	#print 'data_set_filtered 1', data_set_filtered['1']
	# Adicionando um de cada classe aleatoriamente
	for c, l in data_set.items():
		data_set_filtered[c] = [l.pop(random.randint(0, len(l)-1))]
					
	#print 'data_set_filtered 2', data_set_filtered['2']
	#print len(data_set_filtered['2'])
	while(changed):	
		changed = False
			
		for c, l in data_set.items():
			for li in l:
			
				if not changed:
					li_class = knn_euclidian((solution[0], solution[1], 1), data_set_filtered, li)
				
					if li_class != c:
						changed = True
						data_set_filtered[c].append(l.pop(l.index(li)))						

				
	return data_set_filtered

def tomek_links(solution, data_set):
	"""
	Tomek Links selection of prototypes

	@type data_set: dict
	@param data_set: The original data set

	@rtype: dcit
	@returns: The consistent subset of the original data set 
	"""
	
	tomek_instances = list()
	
	for c, l in data_set.items():
		for li in l:
			near_instance = (1000000, [])

			for c1, l1 in data_set.items():
				for l1i in l1:
				
					if l1i != li:
						d = euclidian_distance(li, l1i, solution)
						
						if d < near_instance[0]:
							near_instance = (d, l1i)
	 		
			if (li[-1:] != near_instance[1][-1:]):
				tomek_instances.append(li)
				tomek_instances.append(near_instance[1])

	
	for t in tomek_instances:
		try:
			del data_set[t[-1:]][data_set[t[-1:]].index(t)]
		except ValueError:
			pass
	
	return data_set



def oss(solution, data_set_):
	"""
	One-Side Selection of prototypes

	@type data_set_: dict
	@param data_set_: The original data set

	@rtype: dcit
	@returns: The consistent subset of the original data set 
	"""

	data_set = cnn(solution, data_set_.copy())

	tomek_instances = list()
	
	for c, l in data_set.items():
		for li in l:
			near_instance = (1000000, [])

			for c1, l1 in data_set.items():
				for l1i in l1:
				
					if l1i != li:
						d = euclidian_distance(li, l1i, solution)
						
						if d < near_instance[0]:
							near_instance = (d, l1i)

			if (li[-1:][0] != near_instance[1][-1:][0]):
				tomek_instances.append(li)
				tomek_instances.append(near_instance[1])

	for t in tomek_instances:
		try:
			del data_set[t[-1:][0]][data_set[t[-1:][0]].index(t)]
		except ValueError:
			pass
	
	return data_set


if __name__ == "__main__":
	"""
	Liver Dataset
	
	data_set = get_liver_dataset('datasets/liver/bupa.data')
	solution = ([1.0]*6, [1]*6, 1)
	
	print 'Original data set distribution'
	for c, l in data_set.items():
		print 'Class', c, ':', len(l)
	
	print ''
	(training_set, test_set) = process_data(data_set, 70)
	print len(test_set['1']) + len(test_set['2']), 'instances will be tested'
	
	print 'Original training data set distribution'
	for c, l in training_set.items():
		print 'Class', c, ':', len(l)
	
	print ''	
        """
	print 'Using OSS'	
	training_set_oss = oss(solution, training_set.copy())
	
	with open('/Users/julianalucena/Desktop/aprendizagem/projeto/projetos-rna-am/datasets/selected/bupa-oss.data', 'w') as f:
		for c, l in training_set_cnn.items():
			for li in l:
				for n in li:
					f.write('%s ' % n)
				f.write('\n')	
	
	print 'final distribution'
	for c, l in training_set_oss.items():
		print 'Class', c, ':', len(l)
	
	""""
	Pima Dataset
	
	data_set = get_pima_dataset('datasets/pima/pima-indians-diabetes.data')		
	solution = ([1.0]*8, [1]*8, 1)

	print 'Original data set distribution'
	for c, l in data_set.items():
		print 'Class', c, ':', len(l)
	
	print ''
	(training_set, test_set) = process_data(data_set, 70)
	print len(test_set['0']) + len(test_set['1']), 'instances will be tested'
	
	print 'Original training data set distribution'
	for c, l in training_set.items():
		print 'Class', c, ':', len(l)
	
	print ''	
	print 'Using OSS'	
	training_set_oss = oss(solution, training_set.copy())
	
	with open('/Users/julianalucena/Desktop/aprendizagem/projeto/projetos-rna-am/datasets/selected/pima-oss1.data', 'w') as f:
		for c, l in training_set_oss.items():
			for li in l:
				for n in li:
					f.write('%s ' % n)
				f.write('\n')	
	
	print 'final distribution'
	for c, l in training_set_oss.items():
		print 'Class', c, ':', len(l)
	"""
	
	"""
	Heart Dataset
	
	data_set = get_heart_dataset('datasets/heart/heart.dat')		
	solution = ([1.0]*13, [1]*13, 1)

	print 'Original data set distribution'
	for c, l in data_set.items():
		print 'Class', c, ':', len(l)
	
	print ''
	(training_set, test_set) = process_data(data_set, 70)
	print len(test_set['1']) + len(test_set['2']), 'instances will be tested'
	
	print 'Original training data set distribution'
	for c, l in training_set.items():
		print 'Class', c, ':', len(l)
	
	print ''	
	print 'Using OSS'	
	training_set_oss = oss(solution, training_set.copy())
	
	with open('/Users/julianalucena/Desktop/aprendizagem/projeto/projetos-rna-am/datasets/selected/heart-oss.data', 'w') as f:
		for c, l in training_set_oss.items():
			for li in l:
				for n in li:
					f.write('%s ' % n)
				f.write('\n')	
	
	print 'final distribution'
	for c, l in training_set_oss.items():
		print 'Class', c, ':', len(l)
	"""
	
	"""
	Australian Dataset
	
	data_set = get_australian_dataset('datasets/australian/australian.dat')		
	solution = ([1.0]*14, [1]*14, 1)

	print 'Original data set distribution'
	for c, l in data_set.items():
		print 'Class', c, ':', len(l)
	
	print ''
	(training_set, test_set) = process_data(data_set, 70)
	print len(test_set['0']) + len(test_set['1']), 'instances will be tested'
	
	print 'Original training data set distribution'
	for c, l in training_set.items():
		print 'Class', c, ':', len(l)
	
	print ''	
	print 'Using OSS'	
	training_set_oss = oss(solution, training_set.copy())
	
	with open('/Users/julianalucena/Desktop/aprendizagem/projeto/projetos-rna-am/datasets/selected/australian-oss.data', 'w') as f:
		for c, l in training_set_oss.items():
			for li in l:
				for n in li:
					f.write('%s ' % n)
				f.write('\n')	
	
	print 'final distribution'
	for c, l in training_set_oss.items():
		print 'Class', c, ':', len(l)
	"""
	
	"""
	Ionosphere Dataset
	
	data_set = get_ionosphere_dataset('datasets/ionosphere/ionosphere.data')		
	solution = ([1.0]*34, [1]*34, 1)
	
	print 'Original data set distribution'
	for c, l in data_set.items():
		print 'Class', c, ':', len(l)
	
	print ''
	(training_set, test_set) = process_data(data_set, 70)
	print len(test_set['g']) + len(test_set['b']), 'instances will be tested'
	
	print 'Original training data set distribution'
	for c, l in training_set.items():
		print 'Class', c, ':', len(l)
	
	print ''	
	print 'Using OSS'	
	training_set_oss = oss(solution, training_set.copy())
	
	with open('/Users/julianalucena/Desktop/aprendizagem/projeto/projetos-rna-am/datasets/selected/ionosphere-oss.data', 'w') as f:
		for c, l in training_set_oss.items():
			for li in l:
				for n in li:
					f.write('%s ' % n)
				f.write('\n')	
	
	print 'final distribution'
	for c, l in training_set_oss.items():
		print 'Class', c, ':', len(l)
	"""
	
	"""
	data_set = get_sonar_dataset('datasets/sonar/sonar.all-data')		
	solution = ([1.0]*60, [1]*60, 1)
	
	print 'Original data set distribution'
	for c, l in data_set.items():
		print 'Class', c, ':', len(l)
	
	print ''
	(training_set, test_set) = process_data(data_set, 70)
	print len(test_set['R']) + len(test_set['M']), 'instances will be tested'
	
	print 'Original training data set distribution'
	for c, l in training_set.items():
		print 'Class', c, ':', len(l)
	
	print ''	
	print 'Using OSS'	
	training_set_oss = oss(solution, training_set.copy())
	
	with open('/Users/julianalucena/Desktop/aprendizagem/projeto/projetos-rna-am/datasets/selected/sonar-oss.data', 'w') as f:
		for c, l in training_set_oss.items():
			for li in l:
				for n in li:
					f.write('%s ' % n)
				f.write('\n')	
	
	print 'final distribution'
	for c, l in training_set_oss.items():
		print 'Class', c, ':', len(l)
	"""
	
	# Tabu search
	best_solution = tabu_search(training_set_oss, test_set, knn_euclidian, solution, 100)
	print 'Hits for the best solution'
	print training_machine(training_set, test_set, knn_euclidian, best_solution)
		
	#for k in range(1, 6):
	  #print 'k', k
	  #print training_machine(training_set, test_set, knn_euclidian, ([1.0, 1.0, 1.0, 1.0, 1.0, 1.0],[1, 1, 1, 1, 1, 1],k))#, adaptative=True)
