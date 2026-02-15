#!/usr/bin/env python3
"""
Non-batch script to generate multiple city reviews using Nova Light with parallel processing
"""
import boto3
import json
import random
from datetime import datetime, timedelta
import time
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading

# Load .env
def load_env():
    env = {}
    with open('../../.env', 'r') as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                env[key] = value
    return env

# 200 cities (exactly)
CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington DC",
    "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore",
    "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Kansas City", "Mesa", "Atlanta", "Colorado Springs", "Raleigh",
    "Omaha", "Miami", "Oakland", "Minneapolis", "Tulsa", "Cleveland", "Wichita", "Arlington", "New Orleans", "Bakersfield",
    "London", "Paris", "Berlin", "Madrid", "Rome", "Amsterdam", "Vienna", "Prague", "Budapest", "Warsaw",
    "Stockholm", "Copenhagen", "Oslo", "Helsinki", "Dublin", "Edinburgh", "Brussels", "Zurich", "Geneva", "Barcelona",
    "Milan", "Naples", "Florence", "Venice", "Munich", "Hamburg", "Frankfurt", "Cologne", "Stuttgart", "Düsseldorf",
    "Lisbon", "Porto", "Athens", "Thessaloniki", "Istanbul", "Ankara", "Kiev", "Moscow", "St Petersburg", "Minsk",
    "Riga", "Vilnius", "Tallinn", "Ljubljana", "Zagreb", "Belgrade", "Sarajevo", "Skopje", "Sofia", "Bucharest",
    "Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya", "Sapporo", "Kobe", "Fukuoka", "Sendai", "Hiroshima",
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Suwon", "Ulsan", "Changwon", "Goyang",
    "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Hangzhou", "Wuhan", "Xi'an", "Suzhou", "Zhengzhou",
    "Tianjin", "Harbin", "Kunming", "Dalian", "Taiyuan", "Urumqi", "Lanzhou", "Hefei", "Changchun", "Shijiazhuang",
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri", "Patna", "Vadodara",
    "Bangkok", "Manila", "Jakarta", "Kuala Lumpur", "Singapore", "Ho Chi Minh City", "Hanoi", "Phnom Penh", "Yangon", "Dhaka",
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle", "Canberra", "Sunshine Coast", "Wollongong",
    "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Kitchener",
    "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza", "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Goiânia"
]

# More diverse and realistic names
NAMES = [
    "Alex Johnson", "Sarah Chen", "Mike Rodriguez", "Emma Thompson", "David Kim", "Lisa Wang", 
    "James Wilson", "Maria Garcia", "Chris Brown", "Amy Davis", "Ryan Miller", "Jessica Lee", 
    "Matt Wilson", "Nicole Taylor", "Kevin Clark", "Ashley White", "Priya Patel", "Carlos Mendez",
    "Fatima Al-Rashid", "Jake Thompson", "Zoe Martinez", "Raj Singh", "Sophie Dubois", "Omar Hassan",
    "Isabella Romano", "Tyler Brooks", "Aisha Johnson", "Lucas Anderson", "Maya Nakamura", "Ben Foster",
    "Chloe Williams", "Diego Santos", "Nora O'Brien", "Ethan Chang", "Layla Ahmed", "Sam Taylor",
    "Grace Kim", "Jordan Smith", "Aaliyah Brown", "Noah Davis", "Mia Rodriguez", "Liam Wilson"
]

def generate_review_prompt(city, sentiment):
    """Generate a prompt and rating based on city and sentiment with diverse personas and styles"""
    
    # Different persona types for variety
    personas = [
        "a young professional who moved here for work",
        "a family with kids looking for good schools and activities", 
        "a retiree who relocated here for the lifestyle",
        "a college student studying here",
        "a digital nomad who spent 6 months here",
        "a tourist who visited for a week",
        "someone who grew up here and recently moved back",
        "a foodie who explores local restaurants",
        "an outdoor enthusiast who loves hiking and activities",
        "a budget traveler looking for affordable options"
    ]
    
    # Different writing styles
    styles = [
        "Write in a casual, conversational tone like you're texting a friend",
        "Write in a detailed, analytical style with specific examples",
        "Write in a brief, punchy style with short sentences",
        "Write in an emotional, personal storytelling style",
        "Write in a practical, advice-giving tone",
        "Write in an enthusiastic, energetic style with lots of exclamation points",
        "Write in a thoughtful, reflective tone"
    ]
    
    persona = random.choice(personas)
    style = random.choice(styles)
    
    if sentiment == 'positive':
        prompts = [
            f"You are {persona} writing a review of {city}. {style}. Share what you genuinely love about this place - maybe a hidden gem restaurant, a perfect morning routine, or how the city surprised you. Be specific about neighborhoods, local spots, and real experiences. 300-500 words.",
            f"As {persona}, write about why {city} exceeded your expectations. {style}. Focus on authentic moments - that amazing coffee shop, the helpful locals, the perfect weekend activity. Mention specific places and genuine experiences. 300-500 words.",
            f"You're {persona} recommending {city} to a friend. {style}. Talk about the real reasons you'd tell someone to visit or move here. Include practical tips and personal anecdotes. 300-500 words."
        ]
        rating = random.choice([4, 4, 5])
    elif sentiment == 'negative':
        prompts = [
            f"You are {persona} writing an honest review about the challenges of {city}. {style}. Share specific frustrations - maybe the commute, cost of living, or something that didn't work for your lifestyle. Be fair but honest about real problems. 300-500 words.",
            f"As {persona}, explain why {city} wasn't the right fit for you. {style}. Focus on concrete issues you experienced - not just complaints, but real situations that affected your daily life. 300-500 words.",
            f"You're {persona} giving a heads-up to others about {city}'s downsides. {style}. Share what you wish you'd known before visiting/moving. Be constructive in your criticism. 300-500 words."
        ]
        rating = random.choice([1, 2, 2])
    else:  # neutral
        prompts = [
            f"You are {persona} giving a balanced perspective on {city}. {style}. Share both what worked and what didn't for your situation. Be honest about trade-offs and help others understand if it might be right for them. 300-500 words.",
            f"As {persona}, write a realistic review of {city}. {style}. Cover the good, the bad, and the 'it depends' aspects. Give practical insights for different types of people. 300-500 words."
        ]
        rating = 3
    
    return random.choice(prompts), rating

def call_nova(prompt, bedrock_client):
    """Call Nova Light to generate a review with varied parameters for authenticity"""
    try:
        # Define the message with proper Nova Light format
        message_list = [{"role": "user", "content": [{"text": prompt}]}]
        
        # Vary temperature and other parameters for more diverse outputs
        temperature = random.uniform(0.6, 0.9)  # More variation in creativity
        top_p = random.uniform(0.8, 0.95)       # Vary nucleus sampling
        
        # Configure inference parameters with randomization
        inf_params = {
            "maxTokens": random.randint(800, 1200),  # Vary response length
            "temperature": temperature,
            "topP": top_p
        }
        
        body = {
            "schemaVersion": "messages-v1",
            "messages": message_list,
            "inferenceConfig": inf_params
        }
        
        response = bedrock_client.invoke_model(
            modelId="us.amazon.nova-lite-v1:0",
            body=json.dumps(body)
        )
        
        response_body = json.loads(response['body'].read())
        return response_body['output']['message']['content'][0]['text']
    
    except Exception as e:
        print(f"Error calling Nova: {e}")
        return None

def generate_single_review(review_task):
    """Generate a single review - designed to be called in parallel"""
    city, sentiment, city_index, review_index, bedrock_client = review_task
    
    try:
        # Generate prompt and rating
        prompt, rating = generate_review_prompt(city, sentiment)
        
        # Call Nova to generate review
        review_text = call_nova(prompt, bedrock_client)
        
        if review_text:
            # Post-process for authenticity
            review_text = make_more_authentic(review_text)
            
            # Add realistic visit dates
            visit_date = None
            if random.random() > 0.3:  # 70% chance of having a visit date
                days_before_submission = random.randint(7, 365)
                visit_date = (datetime.now() - timedelta(days=random.randint(1, 30) + days_before_submission)).strftime('%Y-%m-%d')
            
            # Create unique user ID for each review
            user_id = f"demo-user-{city_index+1:03d}-{review_index+1}"
            
            # Create DynamoDB record
            record = {
                'userId': user_id,
                'submittedAt': (datetime.now() - timedelta(days=random.randint(1, 90))).isoformat() + 'Z',
                'cityName': city,
                'reviewText': review_text,
                'reviewerName': random.choice(NAMES),
                'rating': rating,
                'submittedBy': f"demo{city_index+1:03d}r{review_index+1}@example.com",
                'isGenerated': True
            }
            
            # Add visit date if generated
            if visit_date:
                record['visitDate'] = visit_date
            
            return {
                'success': True,
                'record': record,
                'city': city,
                'sentiment': sentiment,
                'rating': rating,
                'preview': review_text.split('\n')[0][:60] + "..." if len(review_text.split('\n')[0]) > 60 else review_text.split('\n')[0]
            }
        else:
            return {
                'success': False,
                'city': city,
                'sentiment': sentiment,
                'error': 'Failed to generate review text'
            }
            
    except Exception as e:
        return {
            'success': False,
            'city': city,
            'sentiment': sentiment,
            'error': str(e)
        }

def process_city_reviews_parallel(city_plan, city_index, bedrock_client, table, max_workers=5):
    """Process all reviews for a single city in parallel"""
    city = city_plan['city']
    num_reviews = city_plan['num_reviews']
    sentiments = city_plan['sentiments']
    
    print(f"\n🏙️  Processing {city_index+1}/200: {city} ({num_reviews} reviews)")
    
    # Create tasks for parallel processing
    tasks = []
    for review_index in range(num_reviews):
        sentiment = sentiments[review_index]
        task = (city, sentiment, city_index, review_index, bedrock_client)
        tasks.append(task)
    
    # Process reviews in parallel using ThreadPoolExecutor
    successful_uploads = 0
    failed_uploads = 0
    
    with ThreadPoolExecutor(max_workers=min(max_workers, num_reviews)) as executor:
        # Submit all tasks
        future_to_task = {executor.submit(generate_single_review, task): task for task in tasks}
        
        # Process completed tasks
        for future in future_to_task:
            result = future.result()
            
            if result['success']:
                # Upload to DynamoDB
                if upload_to_dynamodb(result['record'], table):
                    successful_uploads += 1
                    print(f"  ✓ {result['sentiment']}: {result['preview']} (rating: {result['rating']})")
                else:
                    failed_uploads += 1
                    print(f"  ✗ {result['sentiment']}: Failed to upload to DynamoDB")
            else:
                failed_uploads += 1
                print(f"  ✗ {result['sentiment']}: {result['error']}")
    
    return successful_uploads, failed_uploads

def make_more_authentic(review_text):
    """Post-process review text to make it more human-like and less AI-generated"""
    import re
    
    # Common AI phrases to replace with more natural alternatives
    ai_phrases = {
        r"I must say": random.choice(["honestly", "to be honest", "I have to say", ""]),
        r"it's worth noting": random.choice(["also", "plus", "another thing", ""]),
        r"overall": random.choice(["all in all", "in the end", "basically", ""]),
        r"in conclusion": random.choice(["bottom line", "so yeah", "anyway", ""]),
        r"I would highly recommend": random.choice(["definitely check out", "you should totally visit", "go for it"]),
        r"it's important to mention": random.choice(["oh and", "also", "btw", ""]),
        r"furthermore": random.choice(["also", "plus", "and", ""]),
        r"additionally": random.choice(["also", "plus", "and", ""])
    }
    
    # Apply replacements
    for ai_phrase, replacement in ai_phrases.items():
        if random.random() > 0.5:  # Only replace 50% of the time
            review_text = re.sub(ai_phrase, replacement, review_text, flags=re.IGNORECASE)
    
    # Add occasional typos/informal language (sparingly)
    if random.random() > 0.8:  # 20% chance
        informal_replacements = {
            r"\bgoing to\b": "gonna",
            r"\bwant to\b": "wanna", 
            r"\bkind of\b": "kinda",
            r"\ba lot of\b": "lots of",
            r"\bpretty good\b": "pretty decent",
            r"\breally good\b": "really solid"
        }
        
        # Pick one random replacement
        phrase, replacement = random.choice(list(informal_replacements.items()))
        review_text = re.sub(phrase, replacement, review_text, flags=re.IGNORECASE)
    
    # Remove overly formal transitions occasionally
    if random.random() > 0.7:  # 30% chance
        review_text = re.sub(r"However, ", "", review_text)
        review_text = re.sub(r"Nevertheless, ", "", review_text)
        review_text = re.sub(r"Moreover, ", "", review_text)
    
    return review_text.strip()

def upload_to_dynamodb(review_data, table):
    """Upload a single review to DynamoDB"""
    try:
        table.put_item(Item=review_data)
        return True
    except Exception as e:
        print(f"Error uploading to DynamoDB: {e}")
        return False

def generate_city_reviews_plan():
    """Generate a plan for how many reviews each city gets and their sentiment distribution"""
    city_plans = []
    
    for city in CITIES:
        # Each city gets 3-5 reviews
        num_reviews = random.randint(3, 5)
        
        # Generate sentiment distribution for this city (positive-heavy)
        sentiments = []
        
        for _ in range(num_reviews):
            # 75% positive, 15% neutral, 10% negative
            rand = random.random()
            if rand < 0.75:
                sentiments.append('positive')
            elif rand < 0.90:
                sentiments.append('neutral')
            else:
                sentiments.append('negative')
        
        city_plans.append({
            'city': city,
            'num_reviews': num_reviews,
            'sentiments': sentiments
        })
    
    # Calculate totals for reporting
    total_reviews = sum(plan['num_reviews'] for plan in city_plans)
    total_positive = sum(plan['sentiments'].count('positive') for plan in city_plans)
    total_neutral = sum(plan['sentiments'].count('neutral') for plan in city_plans)
    total_negative = sum(plan['sentiments'].count('negative') for plan in city_plans)
    
    print(f"Review generation plan:")
    print(f"  Cities: {len(CITIES)}")
    print(f"  Total reviews: {total_reviews}")
    print(f"  Distribution: {total_positive} positive ({total_positive/total_reviews*100:.1f}%), {total_neutral} neutral ({total_neutral/total_reviews*100:.1f}%), {total_negative} negative ({total_negative/total_reviews*100:.1f}%)")
    print(f"  Average reviews per city: {total_reviews/len(CITIES):.1f}")
    
    return city_plans

def main():
    # Load environment variables
    env = load_env()
    table_name = env.get('REVIEWS_TABLE')
    
    if not table_name:
        print("REVIEWS_TABLE not found in .env")
        return
    
    # Initialize AWS clients
    bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table(table_name)
    
    print(f"🚀 Generating multiple reviews per city using Nova Light with PARALLEL processing...")
    print(f"Each city gets 3-5 reviews with positive-heavy distribution")
    print(f"DynamoDB table: {table_name}")
    print("")
    
    # Generate city review plans
    city_plans = generate_city_reviews_plan()
    print("")
    
    # Configuration for parallel processing
    MAX_WORKERS = 5  # Number of concurrent Bedrock calls per city
    
    print(f"⚡ Using parallel processing with up to {MAX_WORKERS} concurrent requests per city")
    print("This should be significantly faster than sequential processing!")
    print("")
    
    successful_uploads = 0
    failed_uploads = 0
    total_reviews_planned = sum(plan['num_reviews'] for plan in city_plans)
    start_time = time.time()
    
    # Process each city with parallel review generation
    for city_index, plan in enumerate(city_plans):
        city_start_time = time.time()
        
        # Process all reviews for this city in parallel
        city_successful, city_failed = process_city_reviews_parallel(
            plan, city_index, bedrock_client, table, MAX_WORKERS
        )
        
        successful_uploads += city_successful
        failed_uploads += city_failed
        
        city_duration = time.time() - city_start_time
        print(f"  ⏱️  City completed in {city_duration:.1f}s ({city_successful} successful, {city_failed} failed)")
        
        # Progress update every 10 cities
        if (city_index + 1) % 10 == 0:
            elapsed_time = time.time() - start_time
            avg_time_per_city = elapsed_time / (city_index + 1)
            estimated_remaining = avg_time_per_city * (len(CITIES) - city_index - 1)
            
            print(f"\n📊 Progress: {city_index+1}/200 cities processed")
            print(f"   Reviews: {successful_uploads + failed_uploads}/{total_reviews_planned} ({successful_uploads} successful, {failed_uploads} failed)")
            print(f"   ⏱️  Elapsed: {elapsed_time/60:.1f}m, Estimated remaining: {estimated_remaining/60:.1f}m")
            print(f"   📈 Average: {avg_time_per_city:.1f}s per city")
    
    total_duration = time.time() - start_time
    
    print(f"\n🎉 === Final Results ===")
    print(f"Cities processed: {len(CITIES)}")
    print(f"Total reviews planned: {total_reviews_planned}")
    print(f"Successful uploads: {successful_uploads}")
    print(f"Failed uploads: {failed_uploads}")
    print(f"Success rate: {(successful_uploads/total_reviews_planned*100):.1f}%")
    print(f"⏱️  Total time: {total_duration/60:.1f} minutes ({total_duration/3600:.1f} hours)")
    print(f"📈 Average time per city: {total_duration/len(CITIES):.1f}s")
    print(f"📈 Average time per review: {total_duration/successful_uploads:.1f}s")
    
    if successful_uploads > 0:
        print(f"\n✅ Done! Check your app for the new reviews.")
        print(f"Reviews uploaded to DynamoDB table: {table_name}")
        print(f"Average reviews per city: {successful_uploads/len(CITIES):.1f}")
        
        # Estimate time savings
        estimated_sequential_time = successful_uploads * 2  # Assume 2s per review sequentially
        time_saved = estimated_sequential_time - total_duration
        if time_saved > 0:
            print(f"⚡ Parallel processing saved approximately {time_saved/60:.1f} minutes!")

if __name__ == "__main__":
    main()
