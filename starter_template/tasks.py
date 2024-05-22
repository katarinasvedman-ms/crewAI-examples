from crewai import Task
from textwrap import dedent
from datetime import date


class TripTasks():    

  def identify_task(self, agent, origin, cities, interests, range):
    return Task(description=dedent(f"""\
        "If only one city is given as input here: {cities}, then the task involves analyzing ONLY that city's upcoming events, and travel costs. 
        The goal is to provide a detailed report on the chosen city, and everything you found out about it, 
        including the actual flight costs  and attractions traveling from: {origin}, 
        Trip Date: {range}, Traveler Interests: {interests}. Consider specific criteria such as seasonal events, and travel costs. 
        If more than one city is specified here: {cities}, then this task involves to select the best city from the list of given options: {cities}, 
        considering factors like current weather conditions, upcoming cultural or seasonal events, and overall travel expenses.
        If you do your BEST WORK, I'll tip you $100!"""),
        expected_output='A detailed report on the chosen city, and everything you found out about it, including the actual flight costs and attractions.',
        agent=agent)

  def gather_task(self, agent, origin, interests, range):
    return Task(description=dedent(f"""\
        As a local expert on this city you must compile an 
        in-depth guide for someone traveling there and wanting 
        to have THE BEST trip ever!
        Gather information about  key attractions, local customs,
        special events, and daily activity recommendations.
        Find the best spots to go to, the kind of place only a
        local would know.
        This guide should provide a thorough overview of what 
        the city has to offer, including hidden gems, cultural
        hotspots, must-visit landmarks and
        high level costs.        
        
        {self.__tip_section()}

        Trip Date: {range}
        Traveling from: {origin}
        Traveler Interests: {interests}
      """),
      expected_output='The final answer must be a comprehensive city guide, rich in cultural insights and practical tips, tailored to enhance the travel experience.',
                agent=agent)

  def plan_task(self, agent, origin, interests, range):
    return Task(description=dedent(f"""\
        Expand this guide into a a full 7-day travel 
        itinerary with detailed per-day plans, including places to eat, packing suggestions, 
        and a budget breakdown.
        
        You MUST suggest actual places to visit, actual hotels 
        to stay and actual restaurants to go to.
        
        This itinerary should cover all aspects of the trip, 
        from arrival to departure, integrating the city guide
        information with practical travel logistics.
        
        {self.__tip_section()}

        Trip Date: {range}
        Traveling from: {origin}
        Traveler Interests: {interests}
      """),
      expected_output='Your final answer MUST be a complete expanded travel plan, formatted as markdown, encompassing a daily schedule, anticipated seasonal weather conditions, recommended clothing and items to pack, and a detailed budget, ensuring THE BEST TRIP EVER, Be specific and give it a reason why you picked up each place, what make them special!',
                agent=agent)

  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"
