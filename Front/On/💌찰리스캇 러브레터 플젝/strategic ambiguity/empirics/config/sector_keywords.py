"""
Sector Classification Keywords Configuration

This module defines keyword lists for classifying companies into different sectors.
Each sector has a list of keywords used for text matching in company descriptions.

Version History:
- 1.0 (2025-10-26): Initial implementation with AV, 3DP, AI_ML, Robotics, Software, Hardware
- 1.1 (2025-10-26): Enhanced AI_ML keywords, added research-focused terms

Usage:
    from config.sector_keywords import SECTOR_DEFINITIONS, get_sector_keywords
    
    # Get all sectors
    sectors = get_all_sectors()  # ['AV', '3DP', 'AI_ML', ...]
    
    # Get keywords for specific sector
    av_keywords = get_sector_keywords('AV')
"""

SECTOR_DEFINITIONS = {
    'AV': {
        'name': 'Autonomous Vehicles',
        'description': 'Companies developing self-driving vehicles and related technologies',
        'keywords': [
            # Core autonomous vehicle terms
            'autonomous vehicle', 'self-driving', 'autonomous driving',
            'driverless', 'vehicle automation', 'autonomous car',
            
            # Sensor technologies
            'lidar', 'radar sensor', 'perception system', 'sensor fusion',
            'computer vision for vehicles', 'automotive perception',
            
            # Software/algorithms
            'adas', 'advanced driver assistance', 'path planning',
            'motion planning', 'automotive ai', 'driving policy',
            'lane detection', 'object detection vehicle',
            
            # Industry-specific
            'waymo', 'cruise', 'autonomous fleet', 'robotaxi',
            'autonomous trucking', 'autonomous delivery vehicle'
        ],
        'version': '1.0',
        'last_updated': '2025-10-26'
    },
    
    '3DP': {
        'name': '3D Printing',
        'description': 'Additive manufacturing and 3D printing technologies',
        'keywords': [
            # Core terms
            '3d print', 'additive manufacturing', 'additive fabrication',
            'rapid prototyping', '3d fabrication',
            
            # Technologies
            'stereolithography', 'selective laser sintering', 'sls',
            'selective laser melting', 'slm', 'fused deposition',
            'fused filament', 'fdm', 'fused deposition modeling',
            'sla', 'direct metal laser', 'dmls',
            
            # Applications
            'metal printing', 'bioprinting', 'tissue printing',
            'powder bed fusion', 'material extrusion',
            'binder jetting', 'material jetting',
            
            # Industry-specific
            'prosthetic printing', 'dental printing', 'aerospace additive'
        ],
        'version': '1.0',
        'last_updated': '2025-10-26'
    },
    
    'AI_ML': {
        'name': 'AI/Machine Learning',
        'description': 'Artificial intelligence and machine learning technologies',
        'keywords': [
            # Core AI/ML terms
            'artificial intelligence', 'machine learning', 'deep learning',
            'neural network', 'AI', 'ML', 'neural',
            
            # Natural language processing
            'NLP', 'natural language processing', 'natural language',
            'language model', 'large language model', 'llm',
            'GPT', 'generative AI', 'gen ai', 'generative model',
            'transformer', 'bert', 'text generation',
            
            # Conversational AI
            'chatbot', 'conversational AI', 'dialogue system',
            'virtual assistant', 'AI assistant',
            
            # Computer vision
            'computer vision', 'image recognition', 'object detection',
            'image classification', 'vision model', 'image synthesis',
            
            # Other ML subfields
            'reinforcement learning', 'supervised learning',
            'unsupervised learning', 'transfer learning',
            'few-shot learning', 'zero-shot learning',
            'recommendation system', 'recommendation engine',
            
            # Applied AI
            'AI platform', 'machine learning platform', 'MLops',
            'AI infrastructure', 'model serving', 'AI training'
        ],
        'version': '1.1',
        'last_updated': '2025-10-26'
    },
    
    'Robotics': {
        'name': 'Robotics',
        'description': 'Robotic systems and automation technologies',
        'keywords': [
            # Core robotics
            'robot', 'robotic', 'robotics', 'robotic system',
            
            # Manipulation
            'manipulation', 'gripper', 'end effector', 'robotic arm',
            'robotic manipulator', 'pick and place',
            
            # Types of robots
            'collaborative robot', 'cobot', 'industrial robot',
            'mobile robot', 'humanoid robot', 'service robot',
            
            # Applications
            'warehouse automation', 'industrial automation',
            'robotic assembly', 'robotic welding',
            'robotic inspection', 'logistics automation',
            
            # Components
            'actuator', 'servo', 'robotic control', 'motion control',
            'trajectory planning', 'inverse kinematics'
        ],
        'version': '1.0',
        'last_updated': '2025-10-26'
    },
    
    'Software': {
        'name': 'Software/SaaS',
        'description': 'Software products, SaaS platforms, and cloud services',
        'keywords': [
            # Core software
            'software', 'saas', 'software as a service',
            'application', 'web application', 'mobile app',
            
            # Cloud/platform
            'cloud', 'cloud platform', 'platform as a service',
            'paas', 'infrastructure as a service', 'iaas',
            'cloud service', 'cloud computing',
            
            # Integration
            'api', 'rest api', 'api platform', 'integration platform',
            'webhook', 'microservice',
            
            # Architecture
            'serverless', 'containerized', 'kubernetes',
            'distributed system', 'scalable platform',
            
            # Delivery
            'web service', 'online platform', 'digital platform',
            'enterprise software', 'b2b software', 'b2c app'
        ],
        'version': '1.0',
        'last_updated': '2025-10-26'
    },
    
    'Hardware': {
        'name': 'Hardware',
        'description': 'Hardware products, semiconductors, and physical devices',
        'keywords': [
            # Core hardware
            'hardware', 'device', 'semiconductor', 'chip',
            
            # Chip types
            'asic', 'fpga', 'gpu', 'processor', 'silicon',
            'system on chip', 'soc', 'integrated circuit',
            
            # Computing hardware
            'ai chip', 'ml accelerator', 'neural processor',
            'tpu', 'tensor processing',
            
            # Other hardware
            'sensor', 'iot device', 'embedded system',
            'edge device', 'edge computing hardware',
            'quantum computer', 'quantum processor',
            
            # Manufacturing
            'fabless', 'semiconductor manufacturing',
            'chip design', 'hardware design'
        ],
        'version': '1.0',
        'last_updated': '2025-10-26'
    }
}


def get_sector_keywords(sector_id):
    """
    Get keywords for a specific sector
    
    Args:
        sector_id (str): Sector identifier (e.g., 'AV', '3DP')
    
    Returns:
        list: List of keyword strings
    
    Raises:
        KeyError: If sector_id not found
    """
    if sector_id not in SECTOR_DEFINITIONS:
        raise KeyError(f"Sector '{sector_id}' not found. Available sectors: {list(SECTOR_DEFINITIONS.keys())}")
    
    return SECTOR_DEFINITIONS[sector_id]['keywords']


def get_all_sectors():
    """
    Get list of all sector IDs
    
    Returns:
        list: List of sector identifiers
    """
    return list(SECTOR_DEFINITIONS.keys())


def get_sector_info(sector_id):
    """
    Get full information for a sector
    
    Args:
        sector_id (str): Sector identifier
    
    Returns:
        dict: Sector information including name, description, keywords, etc.
    """
    if sector_id not in SECTOR_DEFINITIONS:
        raise KeyError(f"Sector '{sector_id}' not found. Available sectors: {list(SECTOR_DEFINITIONS.keys())}")
    
    return SECTOR_DEFINITIONS[sector_id]


def print_sector_summary():
    """Print summary of all sectors and keyword counts"""
    print("\n" + "=" * 80)
    print("SECTOR DEFINITIONS SUMMARY")
    print("=" * 80)
    
    for sector_id, info in SECTOR_DEFINITIONS.items():
        print(f"\n{sector_id} - {info['name']}")
        print(f"  Description: {info['description']}")
        print(f"  Keywords: {len(info['keywords'])} terms")
        print(f"  Version: {info['version']} (last updated: {info['last_updated']})")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Print summary when run directly
    print_sector_summary()
    
    # Show example usage
    print("\nExample Usage:")
    print(f"  All sectors: {get_all_sectors()}")
    print(f"  AV keywords (first 5): {get_sector_keywords('AV')[:5]}")
