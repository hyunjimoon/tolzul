"""
Storytelling Skill Measurement for Company Descriptions

This module provides functions to measure storytelling skill from company
description text. Storytelling skill is distinct from vagueness - a company
can tell a clear, vivid story while still being vague about specifics.

Storytelling Elements Measured:
1. Narrative structure (problem-solution pattern)
2. Vivid/concrete language
3. Emotional language
4. Use of examples and metaphors
5. Character/protagonist presence
6. Temporal flow (journey/transformation)

Version: 1.0
Last Updated: 2025-10-26
"""

import re
from typing import Dict, Tuple


# Storytelling indicators
NARRATIVE_STRUCTURE_WORDS = [
    # Problem/challenge words
    'challenge', 'problem', 'difficulty', 'struggle', 'pain point',
    'obstacle', 'barrier', 'gap', 'need', 'issue',
    
    # Solution/transformation words  
    'solution', 'solve', 'transform', 'enable', 'empower',
    'revolutionize', 'reimagine', 'breakthrough', 'innovation',
    'overcome', 'address', 'tackle'
]

VIVID_LANGUAGE_INDICATORS = [
    # Action verbs (concrete)
    'build', 'create', 'design', 'develop', 'launch',
    'deliver', 'drive', 'power', 'accelerate', 'unlock',
    
    # Sensory/concrete language
    'seamless', 'intuitive', 'powerful', 'robust', 'elegant',
    'cutting-edge', 'state-of-the-art', 'next-generation',
    
    # Scale/impact words
    'transform', 'revolutionize', 'disrupt', 'pioneer', 'lead'
]

EMOTIONAL_LANGUAGE = [
    # Positive emotions
    'excited', 'passionate', 'love', 'believe', 'committed',
    'dedicated', 'proud', 'thrilled', 'inspired',
    
    # Aspirational language
    'vision', 'mission', 'dream', 'imagine', 'future',
    'potential', 'opportunity', 'possibility'
]

EXAMPLE_INDICATORS = [
    # Words that introduce examples/stories
    'for example', 'such as', 'including', 'like',
    'case', 'story', 'instance', 'scenario',
    
    # Specific domains/contexts
    'customers', 'users', 'businesses', 'industries',
    'real-world', 'everyday', 'practical'
]

PROTAGONIST_INDICATORS = [
    # People-focused language
    'customers', 'users', 'people', 'teams', 'businesses',
    'entrepreneurs', 'developers', 'engineers', 'designers',
    
    # Human-centric verbs
    'help', 'enable', 'empower', 'allow', 'let',
    'support', 'assist', 'guide', 'serve'
]

TEMPORAL_FLOW_INDICATORS = [
    # Journey/progression words
    'from', 'to', 'become', 'evolve', 'grow',
    'start', 'begin', 'launch', 'scale',
    'journey', 'path', 'progress', 'advance',
    
    # Transformation markers
    'once', 'now', 'today', 'future', 'next',
    'before', 'after', 'until', 'when'
]

ABSTRACT_JARGON = [
    # Generic tech buzzwords (reduce storytelling)
    'leverage', 'utilize', 'optimize', 'maximize',
    'synergy', 'paradigm', 'ecosystem', 'framework',
    'architecture', 'infrastructure', 'platform',
    'solution', 'system', 'technology'
]


def calculate_storytelling_skill(description: str) -> Dict[str, float]:
    """
    Calculate storytelling skill score from company description
    
    Args:
        description: Company description text
    
    Returns:
        Dictionary with overall score and component scores
        
    Score range: 0-100
    - 0-30: Poor storytelling (jargon-heavy, abstract)
    - 31-50: Basic storytelling (some narrative elements)
    - 51-70: Good storytelling (clear narrative, vivid language)
    - 71-100: Excellent storytelling (compelling story, emotional, vivid)
    """
    if not description or description == '' or str(description) == 'nan':
        return {
            'overall_score': 50,
            'narrative_structure': 0,
            'vivid_language': 0,
            'emotional_language': 0,
            'examples_used': 0,
            'protagonist_focus': 0,
            'temporal_flow': 0,
            'jargon_penalty': 0
        }
    
    text = str(description).lower()
    word_count = len(text.split())
    
    # Prevent division by zero
    if word_count == 0:
        word_count = 1
    
    # 1. Narrative structure (problem-solution pattern)
    narrative_count = sum(1 for word in NARRATIVE_STRUCTURE_WORDS if word in text)
    narrative_score = min(20, narrative_count * 4)  # Max 20 points
    
    # 2. Vivid/concrete language
    vivid_count = sum(1 for word in VIVID_LANGUAGE_INDICATORS if word in text)
    vivid_score = min(20, vivid_count * 3)  # Max 20 points
    
    # 3. Emotional language
    emotional_count = sum(1 for word in EMOTIONAL_LANGUAGE if word in text)
    emotional_score = min(15, emotional_count * 5)  # Max 15 points
    
    # 4. Use of examples
    example_count = sum(1 for word in EXAMPLE_INDICATORS if word in text)
    example_score = min(15, example_count * 4)  # Max 15 points
    
    # 5. Protagonist/character focus
    protagonist_count = sum(1 for word in PROTAGONIST_INDICATORS if word in text)
    protagonist_score = min(15, protagonist_count * 3)  # Max 15 points
    
    # 6. Temporal flow (journey/transformation)
    temporal_count = sum(1 for word in TEMPORAL_FLOW_INDICATORS if word in text)
    temporal_score = min(15, temporal_count * 3)  # Max 15 points
    
    # 7. Jargon penalty (reduces storytelling)
    jargon_count = sum(1 for word in ABSTRACT_JARGON if word in text)
    jargon_density = jargon_count / word_count
    jargon_penalty = min(20, jargon_density * 100)  # Max -20 points
    
    # Calculate overall score
    overall_score = (
        narrative_score +
        vivid_score +
        emotional_score +
        example_score +
        protagonist_score +
        temporal_score -
        jargon_penalty
    )
    
    # Normalize to 0-100 range
    overall_score = max(0, min(100, overall_score))
    
    return {
        'overall_score': round(overall_score, 2),
        'narrative_structure': round(narrative_score, 2),
        'vivid_language': round(vivid_score, 2),
        'emotional_language': round(emotional_score, 2),
        'examples_used': round(example_score, 2),
        'protagonist_focus': round(protagonist_score, 2),
        'temporal_flow': round(temporal_score, 2),
        'jargon_penalty': round(jargon_penalty, 2)
    }


def categorize_storytelling(score: float) -> str:
    """
    Categorize storytelling skill level
    
    Args:
        score: Overall storytelling score (0-100)
    
    Returns:
        Category label
    """
    if score >= 71:
        return 'Excellent'
    elif score >= 51:
        return 'Good'
    elif score >= 31:
        return 'Basic'
    else:
        return 'Poor'


def analyze_storytelling_patterns(description: str) -> str:
    """
    Analyze and describe the storytelling pattern used
    
    Args:
        description: Company description text
    
    Returns:
        Pattern description
    """
    text = str(description).lower()
    
    patterns = []
    
    # Check for problem-solution structure
    has_problem = any(word in text for word in ['challenge', 'problem', 'difficulty', 'pain point'])
    has_solution = any(word in text for word in ['solution', 'solve', 'enable', 'empower'])
    if has_problem and has_solution:
        patterns.append('Problem-Solution')
    
    # Check for transformation narrative
    has_transformation = any(word in text for word in ['transform', 'revolutionize', 'reimagine', 'from', 'to'])
    if has_transformation:
        patterns.append('Transformation')
    
    # Check for customer-centric story
    has_customer_focus = any(word in text for word in ['customers', 'users', 'people', 'help', 'enable'])
    if has_customer_focus:
        patterns.append('Customer-Centric')
    
    # Check for vision/mission narrative
    has_vision = any(word in text for word in ['vision', 'mission', 'believe', 'future'])
    if has_vision:
        patterns.append('Vision-Driven')
    
    if not patterns:
        return 'Technical/Descriptive'
    
    return ' + '.join(patterns)


# Example usage and testing
if __name__ == "__main__":
    # Test examples
    test_descriptions = [
        # Excellent storytelling (AV example)
        """Waymo is building the world's most experienced driver to improve access to 
        mobility while saving thousands of lives now lost to traffic crashes. After 
        starting as the Google Self-Driving Car Project in 2009, we've spent over a 
        decade developing breakthrough technologies that help people get where they're 
        going safely and easily. Today, we're the only company in the world operating 
        fully autonomous ride-hailing services, delivering real value to riders.""",
        
        # Good storytelling (3DP example)  
        """Carbon creates innovative 3D printing technology that enables businesses to 
        rapidly design and manufacture end-use products. Our Digital Light Synthesis 
        technology transforms how products are designed and delivered, empowering 
        engineers to create parts that were previously impossible to make.""",
        
        # Poor storytelling (jargon-heavy)
        """Provider of enterprise software solutions leveraging advanced technology 
        infrastructure to optimize business processes and maximize operational synergies 
        through integrated platform architecture."""
    ]
    
    print("=" * 80)
    print("STORYTELLING SKILL ANALYSIS EXAMPLES")
    print("=" * 80)
    
    for i, desc in enumerate(test_descriptions, 1):
        print(f"\n{'='*80}")
        print(f"Example {i}:")
        print(f"{'='*80}")
        print(desc[:100] + "...")
        
        result = calculate_storytelling_skill(desc)
        pattern = analyze_storytelling_patterns(desc)
        category = categorize_storytelling(result['overall_score'])
        
        print(f"\nOverall Score: {result['overall_score']:.1f}/100 ({category})")
        print(f"Pattern: {pattern}")
        print(f"\nComponents:")
        print(f"  Narrative Structure:  {result['narrative_structure']:.1f}/20")
        print(f"  Vivid Language:       {result['vivid_language']:.1f}/20")
        print(f"  Emotional Language:   {result['emotional_language']:.1f}/15")
        print(f"  Examples Used:        {result['examples_used']:.1f}/15")
        print(f"  Protagonist Focus:    {result['protagonist_focus']:.1f}/15")
        print(f"  Temporal Flow:        {result['temporal_flow']:.1f}/15")
        print(f"  Jargon Penalty:       -{result['jargon_penalty']:.1f}")
