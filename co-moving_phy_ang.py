from astropy.coordinates import SkyCoord
import astropy.units as u

# Function to calculate the separation between two galaxies
def calculate_separation(ra1, dec1, redshift1, ra2, dec2, redshift2):
    # Create SkyCoord objects for the galaxies
    gal1 = SkyCoord(ra=ra1*u.deg, dec=dec1*u.deg, distance=redshift1*u.Mpc, frame='icrs')
    gal2 = SkyCoord(ra=ra2*u.deg, dec=dec2*u.deg, distance=redshift2*u.Mpc, frame='icrs')

    # Calculate the angular separation between the galaxies
    angular_separation = gal1.separation(gal2)

    # Calculate the physical separation between the galaxies
    physical_separation = gal1.separation_3d(gal2)

    return angular_separation, physical_separation

# Example input values
ra1 = 211.715826  # Right Ascension of Galaxy 1 in degrees
dec1 = 0.639363  # Declination of Galaxy 1 in degrees
redshift1 = 0.114320  # Redshift of Galaxy 1

ra2 = 211.775111  # Right Ascension of Galaxy 2 in degrees
dec2 = 0.820451  # Declination of Galaxy 2 in degrees
redshift2 = 0.129680  # Redshift of Galaxy 2

# Calculate the separation between the galaxies
angular_sep, physical_sep = calculate_separation(ra1, dec1, redshift1, ra2, dec2, redshift2)

# Print the results
print("For the galaxies 14472 and 14482")
print("Angular separation:", angular_sep)
print("Physical separation:", physical_sep)
